#!/usr/bin/env python3

# Libraries
import datetime, os, time
from sys import platform 
import hashlib

# Script Name:                  ops401_challenge32.py
# Author:                       Michael Roberts 
# Date of latest revision:      02/20/2024
# Purpose:                      create a python script prints that handles searching on different os's 
# Execution:			        have to run python3 ops401_challenge32.py
# Documentation                 Marco Vazquez helped with his demo and https://devblogs.microsoft.com/scripting/use-windows-powershell-to-search-for-files/  https://chat.openai.com/c/239a4a28-59a6-469c-8a85-4cdd9c192d52  


def linux_search(f, d):
    #went with variables within the main instead
    #file = input('Which file to search? ') 
    #dir_path = input('Which directory to search? ')
    command = str(f'find {str(d)} -name {str(f)} |  wc -l')
    os.system(command)
     

def windows_search(f, d):
    #file = input('Which file to search? ')
    #dir_path = input('Which directory to search? ')
    os.system('Get-ChildItem -Path ' + str(d) + ' -Include *' + str(f) + '* -Recurse -ErrorAction SilentlyContinue')

def hashing_file_python(file_to_hash):
    
    h = hashlib.md5(file_to_hash)
    with open(file_to_hash, 'rb') as file:
        
        # loop
        chunk = 0
        while chunk != b'':
            # read 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)
            print(chunk)
            
    
    # return hex rep of hash digest
    return h.hexdigest()
            
#message = hashing_file('testfile.txt')
#print(message)

if platform == 'linux' or platform == 'linux2':
    print('Linux!')
    filename = input('Which file to search? ')
    dir_path = input('Which directory to search? ')
    print(linux_search(filename, dir_path))
    hasher = hashing_file_python(filename)
    print(hasher)
    size = os.path.getsize(filename) 
    complete_path = dir_path + filename
    print(f'{hasher}{datetime.datetime()}{filename}{size}{complete_path}')
    #or do os.system('md5sum file')
elif platform == 'win32':
    filename = input('Which file to search? ')
    dir_path = input('Which directory to search? ')
    print('Windows!')
    os.system(f'Test-Path {dir_path}')
    windows_search(filename, dir_path)
    # a way to get file hash in windows 
    hasher = os.system(f'Get-FileHash {filename} -a md5')
    size = os.path.getsize(filename) 
    complete_path = dir_path + filename
    print(f'{hasher}{datetime.datetime()}{filename}{size}{complete_path}')