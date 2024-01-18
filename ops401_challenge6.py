#!/usr/bin/env python3

# Libraries
#import datetime
import os
import time
#import sys
from cryptography.fernet import Fernet

# Script Name:                  ops401_challenge6.py
# Author:                       Michael Roberts 
# Date of latest revision:      01/16/2024
# Purpose:                      create a python script that uses fernet and encryption
# Execution:			        run the ops401_challenge6.py or python3 ops401_challenge6.py
# Documentation                 Chap-GPT slightly helped here https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python#file-encryption

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
# In Python, create a script that utilizes the cryptography library to:

# Prompt the user to select a mode:
while True:
    
    # error catching to find make sure only a number from 1 to 4 is input
    try:
        mode = int(input("Please select a mode from the provided options: \n 1. Encrypt a file \n 2. Decrypt a file \n 3. Encrypt a message \n 4. Decrypt a message \n ---option: "))
    except TypeError:
        raise "input a number 1-4"

    # Encrypt a file (mode 1)
    if mode == 1:
        fileToEncrypt = str(input("What is the file path? "))
        NewEncFile = encryptfiles(fileToEncrypt, key)
        # os.remove(fileToEncrypt)
        time.sleep(2)
    # Decrypt a file (mode 2)
    elif mode == 2: 
        fileToDecrypt = str(input("What is the file path? "))
        NewDecFile = decryptfiles(fileToDecrypt, key) 
        # os.remove(fileToDecrypt)
        time.sleep(2)
    # Encrypt a message (mode 3)
    elif mode == 3:
        msgToEncyrpt = str(input("Message to be encrypted: "))
        msgEncrypted = f.encrypt(msgToEncyrpt.encode())
        print(msgEncrypted.decode())
        time.sleep(2)
    # Decrypt a message (mode 4)
    elif mode == 4:
        msgToDecyrpt = str(input("Message to Decrypt: "))
        msgDecrypted = f.decrypt(msgToDecyrpt.encode())
        print(msgDecrypted.decode())
        time.sleep(2)
    else:
        print("that is an invalid option")
        time.sleep(2)
        break




# Encrypt the string if in mode 3.
# Print the ciphertext to the screen.
# Decrypt the string if in mode 4.
# Print the cleartext to the screen.