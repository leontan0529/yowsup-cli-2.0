yowsup is a python library that enables building applications that can communicate with WhatsApp users.
The project started as the protocol engine behind [Wazapp for Meego](https://wiki.maemo.org/Wazapp) and
[OpenWA for BB10](https://www.lowyat.net/2013/5896/try-this-openwhatsapp-for-blackberry-10/). Now as a standalone
library it can be used to power any custom WhatsApp client.

```
updated: 15/05/23
Changes:
- Added /yowsup-cli-2.0/yowsup/env/env_utilities.py
  > Script to retrieve latest MD5 and Version values 

updated: 02-05-2023
yowsup version: 3.3.0
yowsup-cli version: 3.2.1
requires:
- python>=2.7,<=3.7
- consonance==0.1.5
- python-axolotl==0.2.2
- protobuf>=3.6.0
- six==1.10
uses:
 - argparse [yowsup-cli]
 - readline [yowsup-cli]
 - pillow [send images]
 - tqdm [mediasink demo]
 - requests [mediasink demo]
```

## See also

During maintenance of yowsup, several projects have been spawned in order to support different features that get
introduced by WhatsApp. Some of those features are not necessarily exclusive to WhatsApp and therefore it only made
sense to maintain some parts as standalone projects:

- [python-axolotl](https://github.com/tgalal/python-axolotl): Python port of
[libsignal-protocol-java](https://github.com/signalapp/libsignal-protocol-java), providing E2E encryption
- [consonance](https://github.com/tgalal/consonance/): WhatsApp's handshake implementation using Noise Protocol
- [dissononce](https://github.com/tgalal/dissononce):  A python implementation for
[Noise Protocol Framework](https://noiseprotocol.org/)


## Quickstart
 * **[Installation](#installation)**
 * **[yowsup's architecture](https://github.com/tgalal/yowsup/wiki/Architecture)**
 * **[Create a sample app](https://github.com/tgalal/yowsup/wiki/Sample-Application)**
 * **[yowsup-cli](https://github.com/tgalal/yowsup/wiki/yowsup-cli)**

## Installation (Ensure you are root user before proceeding below)
###Prepare system for yowsup-cli-2.0 

1.
```
apt-get update
```


Install using setup.py to pull all Python dependencies, or pip:

```
pip install yowsup
```

### Linux

You need to have installed Python headers (probably from python-dev package) and ncurses-dev, then run
```
python setup.py install
```

### FreeBSD (*BSD)
You need to have installed: py27-pip-7.1.2(+), py27-sqlite3-2.7.11_7(+), then run
```
pip install yowsup
```

### Mac OS
```
python setup.py install
```
Administrators privileges might be required, if so then run with 'sudo'

### Windows

 - Install [mingw](http://www.mingw.org/) compiler
 - Add mingw to your PATH
 - In PYTHONPATH\Lib\distutils create a file called distutils.cfg and add these lines:

```
[build]
compiler=mingw32
```
 - Install gcc: ```mingw-get.exe install gcc```
 - Install [zlib](http://www.zlib.net/)
 - ```python setup.py install```

# License:

As of January 1, 2015 yowsup is licensed under the GPLv3+: http://www.gnu.org/licenses/gpl-3.0.html.
