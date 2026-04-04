import zipfile
from pathlib import Path

DIST = Path('dist')
FOLDERS = [Path('main'), Path('custom')]
FILES = [Path('instructions.yml'), Path('mods_list.json')]

print(f"Начало сборки '{DIST/'sprrp-pack.zip'}'")
with zipfile.ZipFile(DIST / 'sprrp-pack.zip', 'w', compression=zipfile.ZIP_DEFLATED) as release:
    for file in FILES:
        release.write(file)
    for folder in FOLDERS:
        for file_path in folder.rglob('*'):
            if file_path.is_file():
                release.write(file_path, arcname=folder.name / file_path.relative_to(folder))
print(f"Конец сборки '{DIST/'sprrp-pack.zip'}'")
