#!/usr/bin/env python3

import warnings 
from cryptography.utils import CryptographyDeprecationWarning
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=CryptographyDeprecationWarning)
    import scapy.all as scapy
    import argparse

mac="ff:ff:ff:ff:ff:ff"

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="IP range")
    (options) = parser.parse_args()
    return options

def scan(ip, mac):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst=mac)
    arp_request_broadcast = broadcast/arp_request
    ans = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    target_list = []
    for element in ans:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        target_list.append(client_dict)
    return target_list

def print_result(result_list):
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
scan_result = scan(options.target, mac)
print_result(scan_result)

