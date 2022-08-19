#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Variables
cwd = os.getcwd()
main_dir = "test"
rootdir = os.path.join(cwd, main_dir)

# Iterate directories
files = []

for dirpath, _, file in os.walk(rootdir):
    for filename in file:
        files.append(os.path.join(dirpath, filename))

# Decrypt key
with open ("key.txt", "rb") as thekey:
    secretkey = thekey.read()

# Decrypt proc
for file in files:
    with open(file, "rb") as thefile:
        content = thefile.read()
    content_decrypted = Fernet(secretkey).decrypt(content)
    with open(file, "wb") as thefile:
        thefile.write(content_decrypted)

#if __name__ == "__main__":
#    main()
