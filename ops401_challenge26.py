#!/usr/bin/env python3

# Libraries
import logging 
import os 
import datetime

# Script Name:                  ops401_challenge26.py
# Author:                       Michael Roberts 
# Date of latest revision:      02/12/2024
# Purpose:                      create a python script prints to a log
# Execution:			        have to run python3 ops401_challenge26.py
# Documentation                 This is a rework of my ping network down/up checker to add logs to it https://chat.openai.com/share/cf7be740-4b7b-4a99-8e64-1fffbee7161c

    
#!/usr/bin/env python3

def setup_logger():
    log = logging.getLogger("my_logger")
    logging.basicConfig(filename='testlog.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    return log

def ping(ip_address, count=1):
    try:
        response = os.system(f"ping -c {count} {ip_address}")
        cur_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if response == 0:
            logging.info(f"{cur_datetime} Network Active to {ip_address}")
        else: 
            logging.error(f"{cur_datetime} Network Down to {ip_address}")
    except Exception as e:
        logging.exception(e)

def main():
    log = setup_logger()
    log.info('Starting ping')
    ip_address = input("Enter IP address to ping: ").strip()
    if not ip_address:
        logging.error('No IP address provided.')
        return
    ping(ip_address)
    log.info('Ping operation completed')

if __name__ == '__main__':
    main()