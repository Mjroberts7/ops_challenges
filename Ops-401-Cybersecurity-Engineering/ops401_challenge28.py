#!/usr/bin/env python3

# Libraries
import logging, datetime, os, time
from logging.handlers import RotatingFileHandler 

# Script Name:                  ops401_challenge27.py
# Author:                       Michael Roberts 
# Date of latest revision:      02/13/2024
# Purpose:                      create a python script prints to a log and adds rotation handling
# Execution:			        have to run python3 ops401_challenge27.py
# Documentation                 

#logger = logging.getLogger('my_logger')

#handlers
#rotationhandler to logg only a certain amount
rhandler = RotatingFileHandler('testlog.log',maxBytes=200,backupCount=3)
#filehandler set level to handle info messages and below. This can be modified per level (exp.WARNING, CRITICAL)
fhandler = logging.FileHandler('testfile.log')
fhandler.setLevel(logging.INFO)
#streamhandler set level to handle info messages and below. This can be modified per level (exp.WARNING, CRITICAL)
shandler = logging.StreamHandler()
shandler.setLevel(logging.INFO)

#format that we are defining
fformat = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
sformat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#tell formatters to apply a specific handler
fhandler.setFormatter(fformat)
shandler.setFormatter(sformat)

#tell handlers to work with specific logger
#logger.addHandler(rhandler)
#logger.addHandler(fhandler)
#logger.addHandler(shandler)

#logger.warning('warn')
#logger.error('error')

def setup_logger():
    log = logging.getLogger("my_logger")
    logging.basicConfig(filename='testlog.log',
                        level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s'
                        # this line kept throwing an error saying stream and file cant be in the same handlers
                        #handlers=[fhandler, shandler #logging.FileHandler('file.log'), logging.StreamHandler(), logging.RotatingFileHandler('testlog.log',maxBytes=200,backupCount=3)
                        )
    return log
'''
def handle(h):
    handler = RotatingFileHandler('testlog.log',maxBytes=20,backupCount=3)
    h.addHandler(handler)

    for i in range(3):
        logmsg= 'Hello'
        logmsg += str(i)
        h.warning(logmsg)
        print('logging:hello', i)
        #os.system('ls -al')
        time.sleep(1)
'''
# you can customize the count here to ping however many times 
def ping(ip_address, count=10):
    try:
        response = os.system(f"ping -c {count} {ip_address}")
        cur_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if response == 0:
            logging.info(f"{cur_datetime} Network Active to {ip_address}")
        else: 
            logging.error(f"{cur_datetime} Network Down to {ip_address}")
    except Exception as e:
        logging.exception(e)

# added the 3 handlers in line after setting the basic config. the maxbytes and backup count can be adjusted to 
# handle the log size requirements. 
def main():
    log = setup_logger()
    log.addHandler(rhandler)
    log.addHandler(fhandler)
    log.addHandler(shandler)
    log.info('Starting ping')
    ip_address = input("Enter IP address to ping: ").strip()
    if not ip_address:
        logging.error('No IP address provided.')
        return
    ping(ip_address)
    log.info('Ping operation completed')

if __name__ == '__main__':
    main()