#!/usr/bin/env python3
import json
import pathlib
import posixpath
import re
import shutil
import subprocess
import sys
from urllib.parse import quote

repo, stage = map(pathlib.Path, sys.argv[1:3])
docs = stage / 'docs'
docs.mkdir(parents=True)
paths = subprocess.check_output(['git', '-C', str(repo), 'ls-files', '-z']).split(b'\0')
tracked = [p.decode('utf-8') for p in paths if p]
source_suffixes = {'.sh', '.bash', '.zsh', '.py', '.js', '.mjs', '.cjs', '.ts', '.tsx',
                   '.jsx', '.c', '.cc', '.cpp', '.h', '.hpp', '.go', '.rs', '.rb',
                   '.pl', '.php', '.java', '.sql', '.ps1', '.lua',
                   '.service', '.timer', '.socket', '.target', '.path', '.mount',
                   '.automount', '.swap', '.device', '.slice', '.scope'}
paths = []
excluded = set()
for name in tracked:
    path = pathlib.PurePosixPath(name)
    source = repo.joinpath(*path.parts)
    if path.is_absolute() or '..' in path.parts or '\n' in name:
        raise ValueError('Unsafe tracked path')
    if source.is_symlink() or not source.is_file():
        raise ValueError('Tracked path is not a regular file: ' + name)
    with source.open('rb') as f:
        shebang = f.read(2) == b'#!'
    if (any(part.startswith('.git') for part in path.parts) or
            path.suffix.lower() in source_suffixes or shebang or source.stat().st_mode & 0o111):
        excluded.add(name)
    else:
        paths.append(name)
nav = []
aliases = {}
for name in paths:
    path = pathlib.PurePosixPath(name)
    if name == 'README.md':
        aliases[name] = 'index.md'
    elif name.endswith('/README.md') and repo.joinpath(*path.parent.parts, 'index.md').exists():
        aliases[name] = str(path.parent / ('repository-readme-' + name.encode().hex() + '.md'))
    else:
        aliases[name] = name

def markdown(data, name, page):
    text = data.decode('utf-8')
    def rewrite(match):
        dest = match.group(1)
        path, marker, anchor = dest.partition('#')
        if marker:
            anchor = re.sub(r'^(phase-[0-9]+)---', r'\1-', anchor)
        if not path:
            return '](#' + anchor if marker else match.group(0)
        if '://' in path or path.startswith('/'):
            return match.group(0)
        target = posixpath.normpath(posixpath.join(posixpath.dirname(name), path))
        if target not in aliases:
            return match.group(0)
        relative = posixpath.relpath(aliases[target], posixpath.dirname(page) or '.')
        return '](' + relative + (marker + anchor if marker else '')
    def unlink_hidden(match):
        label, dest = match.group(1), match.group(2)
        path = dest.partition('#')[0]
        if not path or '://' in path or path.startswith('/'):
            return match.group(0)
        target = posixpath.normpath(posixpath.join(posixpath.dirname(name), path))
        return label if target in excluded else match.group(0)
    text = re.sub(r'(?<!!)\[([^\]]+)\]\(([^\s)]+)\)', unlink_hidden, text)
    return re.sub(r'\]\(([^\s)]+)', rewrite, text)

for name in paths:
    path = pathlib.PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or '\n' in name:
        raise ValueError('Unsafe tracked path')
    source = repo.joinpath(*path.parts)
    if source.is_symlink() or not source.is_file():
        raise ValueError('Tracked path is not a regular file: ' + name)
    data = source.read_bytes()
    target = docs.joinpath(*path.parts)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    try:
        data.decode('utf-8')
        binary = b'\x00' in data
    except UnicodeDecodeError:
        binary = True
    conflicts = name.endswith('/README.md') and repo.joinpath(*path.parent.parts, 'index.md').exists()
    if name == 'README.md':
        continue
    if binary:
        if name.endswith('.md'):
            target.unlink()
        page = '__repository_files__/' + name.encode().hex() + '.md'
        view = docs / page
        view.parent.mkdir(parents=True, exist_ok=True)
        view.write_text('[' + name.replace(']', '\\]') + '](/raw/' + quote(name) + ')\n', encoding='utf-8')
    elif name.endswith('.md') and not conflicts:
        page = name
        target.write_text(markdown(data, name, page), encoding='utf-8')
    elif conflicts:
        page = str(path.parent / ('repository-readme-' + name.encode().hex() + '.md'))
        view = docs / page
        view.parent.mkdir(parents=True, exist_ok=True)
        view.write_text(markdown(data, name, page), encoding='utf-8')
    else:
        page = '__repository_files__/' + name.encode().hex() + '.md'
        view = docs / page
        view.parent.mkdir(parents=True, exist_ok=True)
        text = data.decode('utf-8')
        longest = max((len(m.group(1)) for line in text.splitlines() if (m := re.match(r'^ {0,3}(`+)', line))), default=0)
        fence = '`' * max(3, longest + 1)
        view.write_text(fence + 'text\n' + text + ('\n' if not text.endswith('\n') else '') + fence + '\n', encoding='utf-8')
    nav.append({name: page})

(docs / 'index.md').write_text(markdown((repo / 'README.md').read_bytes(), 'README.md', 'index.md'), encoding='utf-8')
nav.insert(0, {'README.md': 'index.md'})
manifest = {name: page for entry in nav for name, page in entry.items()}
groups = {'Runbook': {}, 'Architecture': {}, 'Guides': {}, 'Internals': {}, 'Repository': {}}
section_names = {'runbook': 'Runbook', 'architecture': 'Architecture', 'guide': 'Guides', 'internals': 'Internals'}
for name, page in manifest.items():
    if name == 'README.md':
        continue
    parts = pathlib.PurePosixPath(name).parts
    section = section_names.get(parts[0], 'Repository')
    remaining = parts[1:] if parts[0] in section_names else parts
    node = groups[section]
    for part in remaining[:-1]:
        node = node.setdefault(part, {})
    node[remaining[-1]] = page

def markdown_title(name):
    try:
        text = repo.joinpath(*pathlib.PurePosixPath(name).parts).read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return pathlib.PurePosixPath(name).name
    if '\x00' in text:
        return pathlib.PurePosixPath(name).name
    match = re.search(r'^#[ \t]+([^\r\n]+?)[ \t]*$', text, re.MULTILINE)
    return match.group(1) if match else pathlib.PurePosixPath(name).name

markdown_titles = {page: markdown_title(name) for name, page in manifest.items()
                   if pathlib.PurePosixPath(name).suffix.lower() == '.md'}

def nav_items(tree):
    return [{(markdown_titles.get(value, name) if not isinstance(value, dict) else name[:1].upper() + name[1:]):
             nav_items(value) if isinstance(value, dict) else value}
            for name, value in sorted(tree.items(), key=lambda item: (item[0] != 'README.md', item[0].lower()))]

nav = [{markdown_titles['index.md']: 'index.md'}] + [{name: nav_items(group)} for name, group in groups.items() if group]
config = {'site_name': 'Rotom Support', 'docs_dir': '/docs', 'site_dir': '/site',
          'theme': {'name': 'material', 'language': 'en', 'features': ['navigation.tabs', 'navigation.tabs.sticky', 'navigation.sections', 'navigation.top', 'toc.follow', 'search.suggest', 'search.highlight'],
                    'palette': [{'scheme': 'slate', 'primary': 'deep purple', 'accent': 'purple'}]},
          'extra': {'generator': False}, 'nav': nav}
(stage / 'mkdocs.yml').write_text(json.dumps(config), encoding='utf-8')
(stage / 'manifest.json').write_text(json.dumps(manifest), encoding='utf-8')
