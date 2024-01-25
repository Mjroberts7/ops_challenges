#!/usr/bin/env python3

# Libraries
# import datetime
# import os
# import time
# import sys
# from cryptography.fernet import Fernet
from scapy.all import IP, sr1, TCP, ICMP#, sr, send, ARP
import ipaddress

# Script Name:                  ops401_challenge12.py
# Author:                       Michael Roberts 
# Date of latest revision:      01/23/2024
# Purpose:                      create a python script that uses ip address scanning or tcp
# Execution:			        have to run as sudo python3 ops401_challenge12.py
# Documentation                 Chap-GPT slightly helped here https://chat.openai.com/share/b4937d7c-eeed-487e-be35-a03a876fcf1c and roger hubas demo script is from where i started at https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-12/challenges/DEMO.md


# Functions
# ICMP scan for all hosts on a network
def ICMPscan(netadd):
    # implemented error handling to show if there is a problem with the initial network entered then it will show it
    try:
        ip_list = ipaddress.IPv4Network(netadd).hosts()
    except ValueError:
        print("not correct address format")
        return
        
    hosts_count = 0
    # updating ip list with not the loopback or broadcast address
    broadcastaddress = "192.168.2.1"
    loopback = "127.0.0.1"
    if netadd[-2:] == "/24":
        ip_list = [ip_list for ip in ip_list if ip != loopback and ip != broadcastaddress]
    # iterating over pinging every item in list. added error handling to show what the errors are. 
    for host in ip_list:
        try:
            print(f'Pinging {str(host)}')
            response = sr1(
                IP(dst=str(host))/ICMP(),
                timeout=2,
                verbose=0
            )
            print(response)
        except scapy.all.sr1.error as e1:
            print(f'sr1 Error: {host}: {e1}')
        except Exception as e:
            print(f'Error: ping did not work {e}')

# The TCP scan 
def TCPscan():
    
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

    # sends a customizable TCP request
    for p in specific_ports:
        tcp_request = sr1(IP(dst=w)/TCP(sport=int(p), dport=int(p), flags='S'), timeout=1, verbose=0)
    
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


if __name__ == "__main__":
    question = int(input("input 1 or 2: ping(1) or TCP(2)? "))
    if question == int(1):
        network = str(input("Network address + CIDR block?\n"))
        ICMPscan(network)
    elif question == int(2):
        TCPscan()
    else:
        print("try again")