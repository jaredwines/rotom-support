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
             'tools/script': '```\nscript\n', 'binary.bin': b'\x00\xff'}
    for name, contents in files.items():
        path = repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(contents if isinstance(contents, bytes) else contents.encode())
    subprocess.run(['git', '-C', str(repo), 'add', '.'], check=True)
    subprocess.run(['python3', str(builder), str(repo), str(stage)], check=True)
    nav = json.loads((stage / 'mkdocs.yml').read_text())['nav']
    views = json.loads((stage / 'manifest.json').read_text())
    assert set(views) == set(files)
    def leaves(items):
        for entry in items:
            for value in entry.values():
                yield from leaves(value) if isinstance(value, list) else [value]
    assert sorted(leaves(nav)) == sorted(views.values())
    features = json.loads((stage / 'mkdocs.yml').read_text())['theme']['features']
    assert 'navigation.tabs' in features and 'toc.follow' in features
    assert [next(iter(entry)) for entry in nav] == ['Home', 'Repository']
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
