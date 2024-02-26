#!/usr/bin/env python3

# Libraries
import datetime, os, time
from sys import platform 
import hashlib

# Script Name:                  ops401_challenge33.py
# Author:                       Michael Roberts 
# Date of latest revision:      02/21/2024
# Purpose:                      create a python script prints that handles searching on different os's with hash comparing
# Execution:			        have to run python3 ops401_challenge33.py
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
'''
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
'''           
#message = hashing_file('testfile.txt')
#print(message)
#virustotalsearch = str(input('where is the path for the virustotal file? '))
#path_to_demo_file = str(input('where is the path for the demo file? '))

def call_virustotal(h):
    # I made this function from the demo script on https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-33/challenges/DEMO.md
    # The below demo script works in tandem with virustotal-search.py from https://github.com/eduardxyz/virustotal-search, which must be in the same directory.
    # Set your environment variable first to keep it out of your script here.

    apikey = os.getenv('API_KEY_VIRUSTOTAL') # Set your environment variable before proceeding. You'll need a free API key from virustotal.com so get signed up there first. Change back to os.getenv('API_KEY_VIRUSTOTAL')
    hash =  h # Set your hash here. 

    # This concatenates everything into a working shell statement that gets passed into virustotal-search.py
    query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + hash

    return os.system(query)

def lin_hash(f):
    command = f'echo {f} | md5sum | sed "s/-$//"'
    lhash = os.system(f'{command}')
    return lhash

def win_hash(f):
    whash = os.system(f'Get-FileHash {f} -a md5')
    return whash



if __name__ == '__main__':
    if platform == 'linux' or platform == 'linux2':
        print('Linux!')
        filename = input('Which file to search? ')
        dir_path = input('Which directory to search? ')
        print(linux_search(filename, dir_path))
        #hasher = hashing_file_python(filename)
        # This is a much easier way to get a hash in linux
        hasher = lin_hash(filename)
        print(hasher)
        call_virustotal(hasher)
        x = call_virustotal(hasher)
        os.system(f'diff <( md5sum {filename} ) <( md5sum {x} )')
        size = os.path.getsize(filename) 
        complete_path = dir_path + filename
        print(f'{hasher}{datetime.datetime.now()}{filename}{size}{complete_path}')
    elif platform == 'win32':
        filename = input('Which file to search? ')
        dir_path = input('Which directory to search? ')
        print('Windows!')
        os.system(f'Test-Path {dir_path}')
        windows_search(filename, dir_path)
        # a way to get file hash in windows 
        hasher = win_hash(filename)
        call_virustotal(hasher)
        y = call_virustotal(hasher)
        size = os.path.getsize(filename) 
        complete_path = dir_path + filename
        os.system(f'Get-DfsrFileHash -Path "{complete_path}"')
        print(f'{hasher}{datetime.datetime.now()}{filename}{size}{complete_path}')

