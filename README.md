<p align="center">
  <b>SPRRP</b>
</p>

<p align="center">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/devmoded/SPRRP?style=for-the-badge">
  <img alt="GitHub Release" src="https://img.shields.io/github/v/release/devmoded/SPRRP?style=for-the-badge">
</p>

<p align="center">
  <img alt="Minecraft version" src="https://img.shields.io/badge/Minecraft-1.20.1-blue?style=for-the-badge">
  <img alt="Fabric version" src="https://img.shields.io/badge/fabric-0.18.4-blue?style=for-the-badge">
</p>

# Важное
Сборка была перенесена с версии 1.16.5 и загрузчика Forge на 1.20.1 с 
загрузчиком Fabric, то есть

```sh
1.16.5 + Forge => 1.20.1 + Fabric
```

Старую версию можно [посмотреть здесь](https://github.com/devmoded/SPRRP/tree/v1.1.0), 
а [скачать тут](https://github.com/devmoded/SPRRP/releases/tag/v1.1.0)

# Системные требования
Минимальных и рекомендуемых требований нет, так как нет возможности это 
как-либо определить ` ┐(￣ヘ￣;)┌ `

# Установка
Для базовой установки достаточно использовать мою программу [Modpack Installer](https://github.com/devmoded/modpack_installer)

# Дополнительная настройка
## Автоматическая доп. настройка
Эту настройку можно выполнить либо вручную, как описано ниже, либо 
воспользоваться скриптом [`custom_install.py`](https://github.com/devmoded/SPRRP/blob/main/custom_install.py)

## Ручная
В каталоге (папке) `modpack_installer/` есть каталог (папка) `custom/`, внутри 
три `.zip` архива:

### `emotes (1).zip`
Его необходимо распаковать, и внутри него будут папка `emotes`, её необходимо
поместить в основную папку игры (сборки)

### `Карта.zip`
Его необходимо распаковать, и внутри него будут папка `XaeroWorldMap`(1) и 
файл `xaeroworldmap.txt`(2)

Первый необходимо скопировать в основную папку игры, второй в папку `config/`

### `Миникарта.zip`
Его необходимо распаковать, и внутри него будут папка `XaeroWaypoints`(1) и 
файл `xaerominimap.txt`(2)

Первый необходимо скопировать в основную папку игры, второй в папку `config/`

## Доп. настройка внутри игры
### Ресурспаки применять в следующем порядке:
1. `verynicetex`
2. `Деньги_Ver2`
3. `деньги`
4. `Unity-1.16.X-Dark-0.7.0`
