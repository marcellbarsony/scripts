#!/usr/bin/env python3

# Import & Remove warnings (will be fixed in Scapy 2.5.0+)
# https://github.com/paramiko/paramiko/issues/2038
import warnings 
from cryptography.utils import CryptographyDeprecationWarning
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=CryptographyDeprecationWarning)
    import scapy.all as scapy
    #from scapy.all import *

# Create ARP request
def scan(ip):
    arp_request = scapy.ARP()
    print(arp_request.summary())
    scapy.ls(scapy.ARP())

scan("10.0.2.1/24")
