import json

from pathlib import Path

from scripts.load_prism_mods_index import get_mods_urls

MODS_LIST = Path('mods_list.json')

mods_list = {
    'loader': 'fabric',
    'mc_version': '1.21.1',
    'mods': get_mods_urls()
}

MODS_LIST.write_text(json.dumps(mods_list, indent=2))
