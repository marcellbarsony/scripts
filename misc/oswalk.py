#!/usr/bin/env python3

import os

path = os.getcwd()

for dirpath, dirname, files, in (os.walk(path)):
    print(f"Dirpath: {dirpath}" )
    print(f"Dirnames: {dirname}" )
    print(f"Files: {files}" )

