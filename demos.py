#!/usr/bin/env python3

# Libraries
# import datetime
# import os
# import time
# import sys
# from cryptography.fernet import Fernet
from scapy.all import IP, sr1, TCP, ICMP#, sr, send, ARP
import ipaddress

host = "192.168.1.158"

response = sr1(IP(dst=str(host))/ICMP(), timeout=2, verbose=0)

print(response)