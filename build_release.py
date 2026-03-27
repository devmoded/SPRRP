import zipfile
from pathlib import Path

DIST = Path('dist')
FOLDERS = [Path('main'), Path('custom')]
with zipfile.ZipFile(DIST / 'sprrp-pack.zip', 'w', compression=zipfile.ZIP_DEFLATED) as release:
    for folder in FOLDERS:
        for file_path in folder.rglob('*'):
            if file_path.is_file():
                release.write(file_path, arcname=folder.name / file_path.relative_to(folder))
