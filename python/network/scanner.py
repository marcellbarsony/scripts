#!/usr/bin/env python3

# Import & Remove warnings (will be fixed in Scapy 2.5.0+)
# https://github.com/paramiko/paramiko/issues/2038
import warnings 
from cryptography.utils import CryptographyDeprecationWarning
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=CryptographyDeprecationWarning)
    import scapy.all as scapy
    #from scapy.all import *

ip="10.0.2.1/24"
mac="ff:ff:ff:ff:ff:ff"

def scan(ip, mac):
    # ARP layer
    arp_request = scapy.ARP(pdst=ip)
    # Ether layer
    broadcast = scapy.Ether(dst=mac)

    # Ethernet frame
    arp_request_broadcast = broadcast/arp_request

    # Send & Capture packet
    # Requires 'sudo -E' to preserve environment
    # https://python-forum.io/thread-36293.html
    #ans, unans = scapy.srp(arp_request_broadcast, timeout=1)
    ans = scapy.srp(arp_request_broadcast, timeout=1)[0]
    for element in ans:
        print(element)
        print("-----")
    #print(ans.summary())

    # Show
    #arp_request_broadcast.show()
    
    # Summary
    #print(arp_request.summary())
    #print(broadcast.summary())
    #print(arp_request_broadcast.summary())
    
    # Get info
    #scapy.ls(scapy.ARP())
    #scapy.ls(scapy.Ether())

scan(ip, mac)
