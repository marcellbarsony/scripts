#!/usr/bin/env python3

import os

cwd = os.getcwd()

for file in (os.listdir(cwd)):
    print(file)
