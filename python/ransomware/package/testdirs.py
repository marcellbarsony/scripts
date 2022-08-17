#!/usr/bin/env python3

import os

cwd = os.getcwd()
main_dir = "test"
rootdir = os.path.join(cwd, main_dir)
directories = [ "test1", "test2", "test3", "test4", "test5" ]
filename = "test.txt"

def tree_structure():

    def create_dirs():
        os.makedirs(rootdir)
        for dir in directories:
            layer1 = os.path.join(rootdir, dir)
            os.makedirs(layer1)
            for dir in directories:
                layer2 = os.path.join(layer1, dir)
                os.makedirs(layer2)
        create_files()

    def create_files():
        for subdir, _, _ in os.walk(rootdir):
            with open(os.path.join(subdir, filename), "w") as file:
                 file.write("Test")

    create_dirs()