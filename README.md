# Avgle.downloader

## Required
- python3
  - requests

```
usage: main.py [-h] [-l login-file] vid [vid ...]

if you need login, follow the format of login.txt, then
    main.py -l <filename> 12345

positional arguments:
  vid            https://avgle.com/video/<vid>

optional arguments:
  -h, --help     show this help message and exit
  -l login-file  A filename contains your account informaion
```