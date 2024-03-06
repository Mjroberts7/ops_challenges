#!/usr/bin/python3

# Libraries
import nmap

# Author:                       Roger Huba
# Date:                         03/05/2024
# Modified by:                  Michael Roberts
# Modified Script Name:         ops401_challenge42.py
# Purpose:                      Nmap script 
# Execution:			        have to run python3 ops401_challenge42.py or make the file executable
# Documentation                 



scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) NSE Script             \n""")
print("You have selected option: ", resp)

range = '1-50'

cust_p_range = input('what port range would you like to scan? ') or range

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    # tested with port 22 works. may need some tweaking to do more than one port on line 50
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, cust_p_range, '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print(scanner[ip_addr]['udp'][int(cust_p_range)]['state'])
elif resp == '3':
    # tested with port sshv1.nse works. may need tweaking if running a different nse on line 59
    nse_script = input('what script would you like to run? ')
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, cust_p_range, arguments=f'--script=/usr/share/nmap/scripts/{nse_script}')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print(scanner[ip_addr]['tcp'][int(cust_p_range)]['state'])
elif resp >= '4':
    print("Please enter a valid option")
