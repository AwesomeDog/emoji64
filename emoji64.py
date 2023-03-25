#!/usr/bin/env python3

import argparse
import base64
import io
import sys

MAGIC = 128512 - 43


def emoji64Encode(s):
    b64 = base64.b64encode(bytes(s, 'UTF-8')).decode('UTF-8')
    return ''.join(map(lambda c: chr(ord(c) + MAGIC), list(b64)))


def emoji64Decode(e):
    b64 = ''.join(map(lambda c: chr(ord(c) - MAGIC), list(e.strip())))
    return base64.b64decode(b64).decode('UTF-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='encode text to emoji and back again.')
    parser.add_argument('-d', "--decode", help="switch on decode mode", action="store_true")
    parser.add_argument('text', help="text to encode/decode(can be from pipeline)", type=str, nargs='?', default=None)

    args = parser.parse_args()
    text = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8').read() if args.text is None else args.text

    if args.decode:
        print(emoji64Decode(text))
    else:
        print(emoji64Encode(text))
