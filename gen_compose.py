import json
from pathlib import Path
from string import Template
from urllib.parse import urlparse, unquote

# Mods
PREFIX = "https://github.com/devmoded/SPRRP/raw/refs/heads/main"
SERVER_MODS = Path("server/mods")
EXCLUDED = [
    'fast-ip-ping-v1.0.8-mc1.21.1-fabric.jar',
    'lazy-language-loader-0.3.7.jar',
    'tl_skin_cape_fabric_1.20.2_1.21.1-1.38.jar',
    'tooltipfix-1.1.1-1.20.jar',
    'selectivebounds-fabric-1.21.1-0.0.3.jar',
    'modmenu-11.0.3.jar',
    'zoomify-2.15.2+1.21.1.jar'
]
# Compose
COMPOSE_TEMPLATE = Path('compose.template.yml')
COMPOSE = Path('compose.yml')

def main():
    compose_mods = []

    mods_list = _load_mods_list()
    loader= mods_list.get('loader')
    mc_version = mods_list.get('mc_version')
    mods = mods_list.get('mods')

    if loader is None:
        raise RuntimeError('В \'mods_list.json\' не указано поле \'loader\'')
    if mc_version is None:
        raise RuntimeError('В \'mods_list.json\' не указано поле \'mc_version\'')
    if mods is None:
        raise RuntimeError('В \'mods_list.json\' не указано поле \'mods\'')

    for mod in mods:
        if isinstance(mod, dict) and isinstance(loader, str) and isinstance(mc_version, str):
            mod_url = mod.get('url')
            if mod_url is not None:
                if mod_url.startswith('https://cdn.modrinth.com'):
                    filename = unquote(urlparse(mod_url).path.split('/')[-1])
                    if filename not in EXCLUDED:
                        compose_mods.append(mod_url)
                elif mod_url.startswith('local:'):
                    filename = unquote(urlparse(mod_url.replace('local:', '')).path.split('/')[-1])
                    if filename not in EXCLUDED:
                        compose_mods.append(f"{PREFIX}/{filename}")

    t = Template(COMPOSE_TEMPLATE.read_text())
    # print(t.substitute(mods_list='\n        '.join(mods)))
    COMPOSE.write_text(t.substitute(mods_list='\n        '.join(compose_mods)))

def _load_mods_list() -> dict[str, str | list[dict[str, str]]]:
    mods_list_path = Path('mods_list.json')
    if not mods_list_path.exists():
        raise FileNotFoundError(f"Список модов {mods_list_path} не существует")
    return json.loads(mods_list_path.read_text())

if __name__ == '__main__':
    main()
