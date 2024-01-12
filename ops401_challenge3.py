#!/usr/bin/env python3

# Libraries
import smtplib
import datetime
import os
import time
# import ops401_challenge2
import getpass
import sys

from email.message import EmailMessage

# Script Name:                  ops401_challenge3.py
# Author:                       Michael Roberts 
# Date of latest revision:      01/10/2024
# Purpose:                      create a python script that emails admin if ip is active or inactive 
# Execution:			        run the ops401_challenge3.py or python3 ops401_challenge3.py
# Documentation                 This script builds onto ops401_challenge2.py. Chap-GPT slightly helped here https://chat.openai.com/share/74d401e5-f91e-4e8e-9750-f878a62e4b77 
# Documentation                 https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password-without-echo/ 
# Documentation                 Roger Hubas code helped here https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-03/challenges/ops_challenge_3_demo.py

# uncomment out this bottom line to import the challenge two from github
# python3 ops401_challenge2

# i used a sharklasers temporary email to recieve the email. It just shows that an email was recieved 
# and is for testing. set content will put the variable defined within main into the email body.
def sendEmail(email, p, bodym, b="uadupqbj@sharklasers.com"):
    msg = EmailMessage()
    msg['Subject'] = 'This is a test email'
    msg['From'] = email
    msg['To'] = b
    msg.set_content(bodym)

    # connected to the gmail server to send the email.
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email, p)
        server.send_message(msg)

def pingFunction(specificip, x=1):
    ping = os.system("ping -c " + x + " " + specificip)
    #curDate = datetime.datetime.now()
    if ping == 0:
        success = str("Network Active")
        print(f'{datetime.datetime.now()}{datetime.time()} {success} to {ipAddress}')
        return success 
    else: 
        failure = str("Network Down")
        print(f'{datetime.datetime.now()}{datetime.time()} {failure} to {ipAddress}')
        return failure

if __name__ == '__main__':  
    try:
        ipAddress = str(input("What Ip address? "))
        firstStatus = pingFunction(ipAddress) 

        for i in range(5):
            otherStatus = pingFunction(ipAddress)
            time.sleep(2)

            if "Network Active" in firstStatus or "Network Active" in otherStatus:
                # input for the email
                emailAddr = str(input("enter sender addr: "))
                # input for the password
                passValue = getpass.getpass()
                # burner email
                burner = str(input("enter recipient addr: "))
                # the intended message in the email
                bod = "Network is Active"
                sendEmail(emailAddr, passValue, bod, burner) 
            else: 
                # input for the email
                emailAddr = str(input("enter sender addr: "))
                # input for the password
                passValue = getpass.getpass()
                # burner email
                burner = str(input("enter recipient addr: "))
                # the intended message in the email
                bod = "Network is down"
                sendEmail(emailAddr, passValue, bod, burner) 

        print("Email sent, success!")
    # this handles a multitude of errors. If there is one then the script will just exit
    except (KeyboardInterrupt, TypeError, ValueError, Exception) as error:
        print('\nThis value does not work, exiting', error)
        sys.exit()