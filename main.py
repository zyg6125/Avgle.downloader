#!/usr/bin/env python3
import argparse
import sys

from Avgle import Avgle


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main(args):
    avgle = Avgle()
    if args.loginfile:
        username, password = args.loginfile.read().split('\n')
        avgle.login(username.strip(), password.strip())

    for vid in args.videoids:
        f = avgle.get_download(vid)
        if f['type'] != 'error':
            f['save']()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='''
if you need login, follow the format of login.txt, then
    main.py -l <filename> 12345''')
    parser.add_argument(
        '-l',
        metavar='login-file',
        help='A filename contains your account informaion',
        type=open,
        dest='loginfile')
    parser.add_argument(
        'videoids',
        metavar='vid',
        nargs='+',
        help='https://avgle.com/video/<vid>')

    main(parser.parse_args())
