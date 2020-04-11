# About

`pystrfry` a tool and Python 3 library for Linux for assisting in solving those annoying [`strfry`](http://man7.org/linux/man-pages/man3/strfry.3.html) CTF challenges that seem to be common in CTFs like [ångstromCTF 2020](https://2020.angstromctf.com/).

No additional requirements other than Linux and Python 3.

## CLI Usage

```
$ ./strfry.py --help

usage: strfry.py [-h] [--processid PROCESSID] [--timestamp TIMESTAMP] [--decode] string

a CTF tool for solving those annoying strfry challenges

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

## Python Usage

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
