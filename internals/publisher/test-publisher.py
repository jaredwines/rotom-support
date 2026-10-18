#!/usr/bin/env python3
import json
import pathlib
import subprocess
import tempfile

builder = pathlib.Path(__file__).resolve().parent / 'build-input.py'
with tempfile.TemporaryDirectory() as directory:
    root = pathlib.Path(directory)
    repo, stage = root / 'repo', root / 'stage'
    repo.mkdir()
    subprocess.run(['git', 'init', '-q', str(repo)], check=True)
    files = {'README.md': '# Home\n', '.hidden': 'hidden text\n',
             'section/README.md': '# Section\n', 'section/index.md': '# Index\n',
             'section/topic.md': '# Topic Title\n[Script](../tools/script)\n', 'section/untitled.md': 'No heading\n',
             'tools/script': '#!/bin/sh\nscript\n', 'tools/check.py': 'print(1)\n',
             'tools/run.sh': 'echo ok\n', 'tools/executable': 'data\n',
             'tools/update.service': '[Service]\n', 'tools/update.timer': '[Timer]\n',
             'tools/update.socket': '[Socket]\n', 'binary.bin': b'\x00\xff',
             '.gitignore': 'ignored rule\n', 'section/.gitattributes': 'attributes\n',
             '.github/workflows/check.yml': 'workflow\n'}
    for name, contents in files.items():
        path = repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(contents if isinstance(contents, bytes) else contents.encode())
    (repo / 'tools/executable').chmod(0o755)
    subprocess.run(['git', '-C', str(repo), 'add', '.'], check=True)
    for asset in ('diagram-expand.js', 'diagram-expand.css.js'):
        target = repo / 'internals/publisher' / asset
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((builder.parent / asset).read_bytes())
    subprocess.run(['python3', str(builder), str(repo), str(stage)], check=True)
    nav = json.loads((stage / 'mkdocs.yml').read_text())['nav']
    views = json.loads((stage / 'manifest.json').read_text())
    excluded = {'.gitignore', 'section/.gitattributes', '.github/workflows/check.yml',
                'tools/script', 'tools/check.py', 'tools/run.sh', 'tools/executable',
                'tools/update.service', 'tools/update.timer', 'tools/update.socket'}
    assert set(views) == set(files) - excluded
    assert all(not (stage / 'docs' / name).exists() for name in excluded)
    def leaves(items):
        for entry in items:
            for value in entry.values():
                yield from leaves(value) if isinstance(value, list) else [value]
    assert sorted(leaves(nav)) == sorted(views.values())
    config = json.loads((stage / 'mkdocs.yml').read_text())
    assert {'name': 'mermaid', 'class': 'mermaid'} in config['markdown_extensions'][0]['pymdownx.superfences']['custom_fences']
    assert config['extra_javascript'] == ['assets/rotom-diagrams/diagram-expand.js']
    assert config['extra_css'] == ['assets/rotom-diagrams/diagram-expand.css']
    assert (stage / 'docs/assets/rotom-diagrams/diagram-expand.js').is_file()
    features = config['theme']['features']
    assert 'navigation.tabs' in features and 'toc.follow' in features
    assert [next(iter(entry)) for entry in nav] == ['Home', 'Repository']
    section_nav = next(entry['Section'] for entry in nav[1]['Repository'] if 'Section' in entry)
    assert not any('Tools' in entry for entry in nav[1]['Repository'])
    assert {'Section': views['section/README.md']} in section_nav
    assert {'Index': views['section/index.md']} in section_nav
    assert {'Topic Title': views['section/topic.md']} in section_nav
    assert {'untitled.md': views['section/untitled.md']} in section_nav
    assert (stage / 'docs/index.md').read_text() == files['README.md']
    assert (stage / 'docs' / views['section/README.md']).read_text() == files['section/README.md']
    assert 'hidden text' in (stage / 'docs' / views['.hidden']).read_text()
    assert '[Script](' not in (stage / 'docs' / views['section/topic.md']).read_text()
    assert 'Script' in (stage / 'docs' / views['section/topic.md']).read_text()
    assert '/raw/binary.bin' in (stage / 'docs' / views['binary.bin']).read_text()
    (repo / 'link').symlink_to('README.md')
    subprocess.run(['git', '-C', str(repo), 'add', 'link'], check=True)
    bad = subprocess.run(['python3', str(builder), str(repo), str(root / 'bad')], capture_output=True)
    assert bad.returncode != 0, 'symlinks must stop publication'
print('Publisher source-selection tests passed')
