#!/usr/bin/env python3

# Libraries

from zipfile import ZipFile

testfile = input("what path to zip file? ") 


def get_file():
    word_list = input('What is a good word list file path? ') 
    return word_list

def unzip_zipfile(zipped_file):
    password = get_file() 
    with open(password, 'rb') as file:
        for word in file:
            try:
                print(word)
                with ZipFile(zipped_file) as zf:
                    zf.extractall(pwd=word.strip())
                    print(f'password = {word.decode()}')
                    break
            except RuntimeError as e:
                print(f'{e}')


unzip_zipfile(testfile)
