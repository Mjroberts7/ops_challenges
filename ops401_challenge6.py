#!/usr/bin/env python3

# Libraries
#import datetime
import os
#import time
#import sys
from cryptography.fernet import Fernet

# Script Name:                  ops401_challenge6.py
# Author:                       Michael Roberts 
# Date of latest revision:      01/16/2024
# Purpose:                      create a python script that uses fernet and encryption
# Execution:			        run the ops401_challenge6.py or python3 ops401_challenge6.py
# Documentation                 Chap-GPT slightly helped here https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python


# some notes from class
message = "variable"

message.encode()
message.decode()
key = Fernet.generate_key()

def writekey():
    
    with open("key.key", "wb") as keyfile:
        keyfile.write(key)

def loadkey():
    return open("key.key", "rb").read()

f = Fernet(key)

# In Python, create a script that utilizes the cryptography library to:

# Prompt the user to select a mode:
while True:
    
    mode = str(input("Please select a mode from the provided options: \n 1. Encrypt a file \n 2. Decrypt a file \n 3. Encrypt a message \n 4. Decrypt a message \n option: "))
    
    # Encrypt a file (mode 1)
    if mode == 1:
        fileToEncrypt = str(f"What is the file path for the target file? {writekey(str(input()))})")
        encrypted = f.encrypt(fileToEncrypt)
        os.remove(fileToEncrypt)
    # Decrypt a file (mode 2)
    elif mode == 2: 
        fileToDecrypt = str(f"What is the file path for the target file? {writekey(str(input()))}")
        decrypted = f.decrypt(fileToDecrypt) 
        os.remove(fileToDecrypt)
    # Encrypt a message (mode 3)
    elif mode == 3:
        msgToEncyrpt = str(input("")).encode()
        msgEncrypted = f.encrypt(msgToEncyrpt)
        print(msgEncrypted)
    # Decrypt a message (mode 4)
    elif mode == 4:
        msgToDecyrpt = str(input("")).decode()
        msgDecrypted = f.decrypt(msgToDecyrpt)
        print(msgDecrypted)
    else:
        print("that is an invalid option")
        break




# Encrypt the string if in mode 3.
# Print the ciphertext to the screen.
# Decrypt the string if in mode 4.
# Print the cleartext to the screen.