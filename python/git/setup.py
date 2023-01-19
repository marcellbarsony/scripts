#!/usr/bin/env python3
"""
Author  : Marcell Barsony <mail@domain.com>
Date    : 2022-01-01
"""

import argparse
import os
import sys


def main(args):

    project = args.arg

    if os.path.isfile(project):
        print(f'{project} is a file')
        exit()

    if not os.path.exists(project):
        os.mkdir(project)

    os.chdir(project)
    print(os.getcwd())

    # git remote add origin https://github.com/marcellbarsony/{args.arg}.git


if __name__ == '__main__':
    """ Initialize argparse """

    parser = argparse.ArgumentParser(
                        prog='GitInit',
                        description='Initialize GitHub repository')

    # Project name
    parser.add_argument('arg',
                        help='Positional argument',
                        nargs='?',
                        metavar='')

    args = parser.parse_args()
    main(args)
