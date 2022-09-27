#!/usr/bin/env python3

import netfilterqueue

# iptables -I FORWARD -j NFQUEUE --queue-num 0

def process_packet(packet):
    print(packet)
    packet.drop()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run

