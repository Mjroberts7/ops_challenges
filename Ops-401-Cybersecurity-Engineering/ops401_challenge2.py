#!/usr/bin/env python3

import datetime
import os
import time

# Script Name:                  ops401_challenge2.py
# Author:                       Michael Roberts 
# Date of latest revision:      01/09/2024
# Purpose:                      create a python script that transmits pings every two seconds, assigns success or faulure, and prints some output 
# Execution:			        run the ops401_challenge2.py or python3 ops401_challenge2.py
# Documentation                 Chap-GPT slightly helped here https://chat.openai.com/share/a9c0cb6d-d9cf-4334-9e24-0352a55c8339

# Variables
ipAddress = str(input("What Ip address? "))
x = 1

# Functions
def pingFunction(specificip):
    ping = os.system("ping -c " + str(x) + " " + specificip)
    #curDate = datetime.datetime.now()
    if ping == 0:
        success = str("Network Active")
        return f'{datetime.datetime.now()}{datetime.time()} {success} to {ipAddress}' 
    else: 
        failure = str("Network Down")
        return f'{datetime.datetime.now()}{datetime.time()} {failure} to {ipAddress}'
        

# Loop
# while True:
if __name__ == "__main__":
    i = 0
    while i < 5:
        print(pingFunction(ipAddress))
        time.sleep(2)
        i += 1
