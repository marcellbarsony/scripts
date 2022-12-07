#!/bin/env/python python3

import sys
import socket
from datetime import datetime

# python3 scanner.py <ip>
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Syntax: python3 port_scanner.py <ip>")

try:
    for port in range(50,85):
        print("Scanning port: {}".format(port))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("Execution stopped")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

