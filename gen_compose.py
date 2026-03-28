from pathlib import Path
from string import Template

# Mods
PREFIX = "https://github.com/devmoded/SPRRP/raw/refs/heads/main"
MODS_DIRS = [Path("main/mods"), Path("server/mods")]
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

# prepare mods list
mods = []

for dir in MODS_DIRS:
    for file in dir.iterdir():
        if file.name not in EXCLUDED:
            mods.append(f"{PREFIX}/{file}")

t = Template(COMPOSE_TEMPLATE.read_text())
# print(t.substitute(mods_list='\n        '.join(mods)))
COMPOSE.write_text(t.substitute(mods_list='\n        '.join(mods)))
