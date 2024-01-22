#!/usr/bin/env python3

# Libraries
# import datetime
# import os
# import time
# import sys
# from cryptography.fernet import Fernet
from scapy.all import IP, sr1, TCP, sr #, send, ARP, ICMP,

# Script Name:                  ops401_challenge11.py
# Author:                       Michael Roberts 
# Date of latest revision:      01/22/2024
# Purpose:                      create a python script that uses scapy
# Execution:			        use sudo python3 ops401_challenge11.py
# Documentation                 Chap-GPT slightly helped here 

# difference between sr() and sr1() - sr1() only returns one packet that answered the sent packet.

# The host IP
host = IP()
# A website that we can scan 
w = 'scanme.nmap.org'
# shows the information of the IP
host.show()
# beginning_port_range = 20
# end_port_range = 3389
specific_ports = [21, 22, 23, 80, 443, 3389]

# sniffs and shows basic packet information
# packets = sniff(count=10)
# print(packets)

# sends an ARP request
# arp_request = ARP()

# sends a customizable icmp request
# icmp_request = sr1(IP(dst='scanme.nmap.org'/ICMP()))

# sends a customizable TCP request
for p in specific_ports:
    tcp_request = sr1(IP(dst=w)/TCP(dport=p, flags='S'), timeout=1, verbose=0)
    
    if tcp_request[TCP].flags == 0x12:
        # if you want to send an RST(reset) packet to close an open connection uncomment this one out
        # rst = IP(dst=host)/TCP(dport=p, flags='R')
        # send(rst)
        print(f"port {p} is open") 
        print(tcp_request.show())
    elif tcp_request[TCP].flags == 0x14:
        print(f"port {p} is closed")
        print(tcp_request.show())
    elif tcp_request is None:
        print(f"port {p} is filtered and dropped")
        print(tcp_request.show())



