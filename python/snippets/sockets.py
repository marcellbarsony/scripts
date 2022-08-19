#!/bin/python3

import socket

port = 7777
host = '127.0.0.1'

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


