#!/usr/bin/env python3
"""
Author  : Name Surname <mail@domain.com>
Date    : 2022-01-01
"""

# Standard library
# https://docs.python.org/3/library/
import argparse
import configparser
import csv
import gzip
import logging
import os
import pynput.keyboard
import socket
import sys
import threading
from datetime import date


# Community library
# https://pypi.org
import faker
import nmap
import numpy
import requests
import scapy
import twisted
from bs4 import BeautifulSoup
from cryptography.fernet import Fernet


def main(args):
    print(args.file, args.count, args.verbose)


if __name__ == '__main__':
    """ Initialize argparse """

    parser = argparse.ArgumentParser(
                        prog='Program-Name',
                        description='Program description',
                        epilog='Text at the bottom of help')

    # Required positional argument
    parser.add_argument('file',
                        choices=['foo', 'bar'],
                        default=[sys.stdin],
                        help='Positional argument',
                        nargs='?')

    # Optional flag (Int)
    parser.add_argument('-c',
                        choices=range(1, 10),
                        default=3,
                        help='Optional value',
                        metavar='',
                        required=False,
                        type=int)

    # Optional flag (True/False)
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        rquired=False,
                        help='True/False')

    # Group
    # group = parser.add_m

    args = parser.parse_args()
    main(args)
