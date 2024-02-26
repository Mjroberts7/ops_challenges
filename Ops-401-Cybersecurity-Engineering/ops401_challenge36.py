#!/usr/bin/env python3

# Libraries
import datetime, os, time
 


# Script Name:                  ops401_challenge36.py
# Author:                       Michael Roberts 
# Date of latest revision:      02/26/2024
# Purpose:                      netcat, telnet, or nmap banner grabbing. 
# Execution:			        have to run python3 ops401_challenge36.py
# Documentation                 All from the dome


# Variables
def netcat_function(i, p):
    os.system(f"nc {i} {p}")

def telnet_function(i, p):
    os.system(f"telnet {i} {p}")

def nmap_function(i):
    os.system(f"nmap {i} --top-ports 100")

# Main function
if __name__ == "__main__":
    
    url_or_ip_a = str(input("enter either a url or ip address. ")) or "scanme.nmap.org"
    
    port_number = int(input("enter a port number. "))

    while True:
        try:
            # provide a variable to start the loop of options
            print("1.) perform a netcat banner grab\n2.) perform a telnet banner grab\n3.) perform a nmap banner grab\n4.) exit")
            x = int(input("What would you like to do? "))
            time.sleep(1)
            
            # conditional choose and option from list 
            if x == 1:
                netcat_function(url_or_ip_a, port_number)
                print(datetime.datetime.now())
            elif x == 2:
                telnet_function(url_or_ip_a, port_number)
                print(datetime.datetime.now())
            elif x == 3:
                nmap_function(url_or_ip_a)
                print(datetime.datetime.now())
            elif x == 4:
                break
            else:
                print("Invalid input. Please choose from provided options ")
        except Exception as e:
            print(f"Error something went wrong", e)