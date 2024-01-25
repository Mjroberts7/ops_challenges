#!/usr/bin/env python3

# Libraries
# import datetime
# import os
# import time
# import sys
# from cryptography.fernet import Fernet
from scapy.all import IP, sr1, TCP, ICMP#, sr, send, ARP
import ipaddress

# Script Name:                  ops401_challenge13.py
# Author:                       Michael Roberts 
# Date of latest revision:      01/24/2024
# Purpose:                      create a python script that uses tcp/ip scanning 
# Execution:			        have to run as sudo python3 ops401_challenge13.py
# Documentation                 tried to get Chap-GPT help but didnt really. it slightly helped here https://chat.openai.com/share/93efb0e4-3244-4840-a6d3-4a491a0a8fac
# Documentation                 I got information for line 45 through subtropicalhorsebacks 40112.py script

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
    hostlist = []
    blocklist = [1, 2, 3, 9, 10, 13]
    # updating ip list with not the loopback or broadcast address
    broadcastaddress = "192.168.1.1"
    loopback = "127.0.0.1"
    if netadd[-2:] == "24":
        ip_list = [ip_list for ip in ip_list if ip != loopback and ip != broadcastaddress]

    # iterating over pinging every item in list. added error handling to show what the errors are. 
    for host in ip_list:
        try:
            print(f'Pinging {str(host)}')
            response = sr1(IP(dst=str(host))/ICMP(), timeout=2, verbose=0)
            if response is not None and response.haslayer(ICMP) and hasattr(response[ICMP], 'code') and int(response[ICMP].code) in blocklist:
                print('host is blocking ping')
            elif response is not None:
                print(response.show())
                hostlist.append(host)
                hosts_count += 1
                TCPscan(host)
            else:
                print('host down')    
        #except scapy.all.sr1.error as e1:
        #    print(f'sr1 Error: {host}: {e1}')
        except Exception as e:
            print(f'Error: ping did not work {e}')
    return f'{hosts_count} is up and running'
# The TCP scan 
def TCPscan(n):
    
    # The host IP
    host = IP(dst=str(n))
    # A website that we can scan 
    w = 'scanme.nmap.org'
    # shows the information of the IP
    host.show()
    # beginning_port_range = 20
    # end_port_range = 3389
    specific_ports = [21, 22, 23, 80, 443, 3389]

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
    network = str(input("Network address + CIDR block? "))
    ICMPscan(network)

    