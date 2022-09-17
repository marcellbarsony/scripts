#!/usr/bin/env python3
#
# Usage:
# sudo mac_changer.py -i enp0s3 -m 11:11:11:11:11:11

import optparse
import os
import re
import subprocess

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC address")
    return parser.parse_args()

def test_arguments(interface, mac):
    if mac and interface:
        interfaces = []
        for item in os.listdir('/sys/class/net'):
            interfaces.append(item)
        if interface not in interfaces:
            print(f"Available interfaces: {interfaces}")
            exit()
    else:
        print("MAC or Interface is not defined.")
        exit()

def change_mac(interface, mac):
    print(f"[+] {interface}: Changing MAC address >> {mac}")
    subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "down"])
    subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "address", mac])
    subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "up"])

def get_mac(interface):
    ip_addr_result = subprocess.check_output(["ip", "link", "show", "dev", interface])
    mac_addr_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ip_addr_result))

    if mac_addr_result:
        return mac_addr_result.group(0)
    else:
        print("[-] Could not read MAC address.")
        exit()

os.system('cls' if os.name == 'nt' else 'clear')
(options, arguments) = get_arguments()
test_arguments(options.interface, options.mac)
current_mac = get_mac(options.interface)
change_mac(options.interface, options.mac)

if current_mac == options.mac:
    print(f"[+] {options.interface}: MAC address was successfully changed.")
else:
    print(f"[-] MAC address cannot be changed to {current_mac}")

