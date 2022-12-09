#!/usr/bin/env python3
"""
Author  : John Doe <jdoe@domain.com>
Date    : 2022-01-01
"""

import argparse
import os
import sys

def main(args):
    print(args.file, args.count, args.verbose)

if __name__ == '__main__':
    """ Initialize argparse """

    parser = argparse.ArgumentParser(
                        prog = 'Program-Name',
                        description = 'Program description',
                        epilog = 'Text at the bottom of help')

    # Required positional argument
    parser.add_argument('file',
                        choices=['foo', 'bar'],
                        default=[sys.stdin],
                        help='Positional argument',
                        nargs='?',
                        type=argparse.FileType('w'))

    # Optional flag (Int)
    parser.add_argument('-c',
                        choices=range(1, 10),
                        default=3,
                        help='Store value',
                        metavar='',
                        required=True,
                        type=int)

    # Optional flag (True/False)
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='True/False')

    # Group
    #group = parser.add_m

    args = parser.parse_args()
    main(args)

