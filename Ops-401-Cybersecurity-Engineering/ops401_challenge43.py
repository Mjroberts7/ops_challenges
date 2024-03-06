#!/usr/bin/python3

import socket


# Author:                       Roger Huba
# Date:                         03/06/2024
# Modified by:                  Michael Roberts
# Modified Script Name:         ops401_challenge43.py
# Purpose:                      sockets script
# Execution:			        have to run python3 ops401_challenge43.py or make the file executable
# Documentation                 


sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 3
sockmod.settimeout(timeout)

hostip = input('what ip would you like to scan? ') or '10.0.2.15' 
portno = int(input('what port would you like to scan? ') or  22) 

def portScanner(port):
    if sockmod.connect((hostip, port)): 
        print("Port closed")
    else:
        print("Port open")

portScanner(portno)