# About

`pystrfry` a tool and Python 3 library for Linux for assisting in solving those annoying [`strfry`](http://man7.org/linux/man-pages/man3/strfry.3.html) CTF challenges that seem to be common in CTFs like [ångstromCTF 2020](https://2020.angstromctf.com/) and [DawgCTF 2020](https://umbccd.io/).

No additional requirements other than Linux and Python 3.

# Installation

## PyPi

```
# pip3 install pystrfry
```

## Manual

```
$ git clone https://github.com/arinerron/pystrfry.git
$ cd pystrfry
# python3 setup.py install
```

# Usage

## Command Line Interface

### Help Menu

```
$ strfry --help

usage: strfry [-h] [--processid PROCESSID] [--timestamp TIMESTAMP] [--decode] string

a tool for solving those annoying strfry CTF challenges

positional arguments:
  string                the string to manipulate

optional arguments:
  -h, --help            show this help message and exit
  --processid PROCESSID, --pid PROCESSID, -p PROCESSID
                        process id which called strfry
  --timestamp TIMESTAMP, --ts TIMESTAMP, -t TIMESTAMP
                        unix timestamp when strfry happened
  --decode, -d          switch to decode mode$
```

### Example

```
$ strfry --pid=1337 --ts=1234 "i use arch btw"
ubs twir ec ha

$ strfry --pid=1337 --ts=1234 "ubs twir ec ha" --decode
i use arch btw
```

## Python Library

```
>>> from strfry import *

>>> strfry('i use arch btw', pid=1337, ts=1234)
'ubs twir ec ha'

>>> unstrfry('ubs twir ec ha', pid=1337, ts=1234)
'i use arch btw'

>>> strfry('this will pull the current ts / pid if you dont specify')
'iutihtfwel usnsd  f oyroyi    t p/rphpctlcsle n dleiitu'

>>> strfry('this will pull the current ts / pid if you dont specify')
'ols tupeprn ftod ceit l sehic  rys i tn pwl/uyflhdiiu t'

>>> strfry('this will pull the current ts / pid if you dont specify')
'ft sult f ynn srhp top /eihlew ipi ecdl l itutc rudyois'
```
