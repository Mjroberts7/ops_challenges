#!/usr/bin/env python3

# Libraries
#import datetime
import os
import time
#import sys
from cryptography.fernet import Fernet

# Script Name:                  ops401_challenge7.py
# Author:                       Michael Roberts 
# Date of latest revision:      01/17/2024
# Purpose:                      create a python script that uses fernet and encryption
# Execution:			        run the ops401_challenge7.py or python3 ops401_challenge7.py
# Documentation                 Chap-GPT slightly helped here https://chat.openai.com/share/b26dbd8e-7cae-481b-95a0-7319c79eeb8b

# functions defined 
def writekey():
    enckey = Fernet.generate_key()
    with open("enckey.key", "wb") as keyfile:
        keyfile.write(enckey)

def loadkey():
    return open("enckey.key", "rb").read()

# these three lines write the encryption key from the global function, give a variable to read the key from,
# and mad another variable from which we can encrypt things from.
writekey()
key = loadkey()
f = Fernet(key)

# these are the two functions that encrypt and decrypt files with parameters for filenames and the encryption key
def encryptfiles(filename, key):
    key = key
    with open(filename, "rb") as file:
        filedata = file.read()
    encdata = f.encrypt(filedata)
    with open(filename, "wb") as file:
        file.write(encdata)

def decryptfiles(filename, key):
    key = key
    with open(filename, 'rb') as file:
        encdata = file.read()
    decdata = f.decrypt(encdata)
    with open(filename, "wb") as file:
        file.write(decdata)

# firstdir should be the root or first dir that you want to start at. 
print("We are going to do some recursive encryption/decription")        
time.sleep(3)
while True:

    choice = str(input("do you want to recursively encrypt[e] or decrypt[d]? \n pick d or e : "))
    firstdir = str(input("What is the root path to encrypt or decrypt? "))

    try:
        if choice == str("e"):
            topdown = '.'
            for path, dirs, files in os.walk(firstdir):
                for file in files:
                    filepath = os.path.join(path, file)
                    encryptfiles(filepath, key)
                    print("succesfully recursively encrypted from the provided path\n")
                    time.sleep(2)
        elif choice == str("d"):
            topdown = '.'
            for path, dirs, files in os.walk(firstdir):
                for file in files:
                    filepath = os.path.join(path, file)
                    if os.path.exists(filepath):
                        decryptfiles(filepath, key)
                        print("succesfully recursively decrypted from the provided path\n")
                        time.sleep(2)
                    else:
                        print(f'{filepath} not found')
                        time.sleep(2)


    except ValueError:
        raise ValueError("choose either d or e")