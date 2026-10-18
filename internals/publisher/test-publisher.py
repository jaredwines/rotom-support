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
             'tools/script': '```\nscript\n', 'binary.bin': b'\x00\xff',
             '.gitignore': 'ignored rule\n', 'section/.gitattributes': 'attributes\n',
             '.github/workflows/check.yml': 'workflow\n'}
    for name, contents in files.items():
        path = repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(contents if isinstance(contents, bytes) else contents.encode())
    subprocess.run(['git', '-C', str(repo), 'add', '.'], check=True)
    subprocess.run(['python3', str(builder), str(repo), str(stage)], check=True)
    nav = json.loads((stage / 'mkdocs.yml').read_text())['nav']
    views = json.loads((stage / 'manifest.json').read_text())
    excluded = {name for name in files if any(part.startswith('.git') for part in pathlib.PurePosixPath(name).parts)}
    assert set(views) == set(files) - excluded
    assert all(not (stage / 'docs' / name).exists() for name in excluded)
    tree = subprocess.check_output(['git', '-C', str(repo), 'write-tree'], text=True).strip()
    archive = subprocess.check_output(['git', '-C', str(repo), 'archive', tree])
    raw = root / 'raw'
    raw.mkdir()
    subprocess.run(['tar', '--exclude=.git*', '-xf', '-', '-C', str(raw)], input=archive, check=True)
    assert all(not (raw / name).exists() for name in excluded)
    assert all((raw / name).read_bytes() == (repo / name).read_bytes() for name in files if name not in excluded)
    def leaves(items):
        for entry in items:
            for value in entry.values():
                yield from leaves(value) if isinstance(value, list) else [value]
    assert sorted(leaves(nav)) == sorted(views.values())
    features = json.loads((stage / 'mkdocs.yml').read_text())['theme']['features']
    assert 'navigation.tabs' in features and 'toc.follow' in features
    assert [next(iter(entry)) for entry in nav] == ['Home', 'Repository']
    assert nav[1]['Repository'][2]['section'][0] == {'Section': views['section/README.md']}
    assert (stage / 'docs/index.md').read_text() == files['README.md']
    assert (stage / 'docs' / views['section/README.md']).read_text() == files['section/README.md']
    assert 'hidden text' in (stage / 'docs' / views['.hidden']).read_text()
    assert '````text\n```\nscript\n````' in (stage / 'docs' / views['tools/script']).read_text()
    assert '/raw/binary.bin' in (stage / 'docs' / views['binary.bin']).read_text()
    (repo / 'link').symlink_to('README.md')
    subprocess.run(['git', '-C', str(repo), 'add', 'link'], check=True)
    bad = subprocess.run(['python3', str(builder), str(repo), str(root / 'bad')], capture_output=True)
    assert bad.returncode != 0, 'symlinks must stop publication'
print('Publisher source-selection tests passed')
