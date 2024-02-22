#!/usr/bin/env python3

import os
from sys import platform 

def linux_search(f, d):
    #went with variables within the main instead
    #file = input('Which file to search? ') 
    #dir_path = input('Which directory to search? ')
    command = str(f'find {str(d)} -name {str(f)} |  wc -l')
    return os.system(command)

def call_virustotal(h):
    # I made this function from the demo script on https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-33/challenges/DEMO.md
    # The below demo script works in tandem with virustotal-search.py from https://github.com/eduardxyz/virustotal-search, which must be in the same directory.
    # Set your environment variable first to keep it out of your script here.

    apikey = os.getenv('API_KEY_VIRUSTOTAL') # Set your environment variable before proceeding. You'll need a free API key from virustotal.com so get signed up there first. Change back to os.getenv('API_KEY_VIRUSTOTAL')
    hash =  f'{h}' # Set your hash here. 

    # This concatenates everything into a working shell statement that gets passed into virustotal-search.py
    query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + hash

    os.system(query)

def lin_hash(f):
    command = f'echo {f} | md5sum | sed "s/-$//"'
    lhash = os.system(f'{command}')
    return lhash

if platform == 'linux' or platform == 'linux2':
    print('Linux!')
    filename = input('Which file to search? ')
    dir_path = input('Which directory to search? ')
    print(linux_search(filename, dir_path))
    hasher = lin_hash(filename)
    print(hasher)
    #call_virustotal(hasher)
else:
    print(platform)