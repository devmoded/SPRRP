import os
import tomli
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

index_env = os.getenv('PRISM_INDEX')
if index_env is None:
    raise RuntimeError('Переменная PRISM_INDEX не указана в .env')

PRISM_INDEX = Path(index_env).expanduser()
LOCAL_MODS = Path('main/mods')
LOCAL_MODS_LIST = [m.name for m in LOCAL_MODS.glob('*.jar')]

def get_mods_urls() -> list[dict[str, str]]:
    mods_urls = []
    for file in PRISM_INDEX.iterdir():
        content = tomli.loads(file.read_text())
        download = content.get('download')
        if download is not None:
            url = download.get('url')
            if url and content['filename'] not in LOCAL_MODS_LIST:
                mods_urls.append({
                    'name': content['name'],
                    'url': url,
                    'version': content['x-prismlauncher-version-number']
                })

    for mod in LOCAL_MODS_LIST:
        mods_urls.append({
            'name': mod.removesuffix('.jar'),
            'url': f"local:{LOCAL_MODS/mod}",
            'version': mod.split('-', 1)[-1].removesuffix('.jar')
        })

    return mods_urls
