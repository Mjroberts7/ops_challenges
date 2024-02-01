#!/usr/bin/env python3

# Libraries
import time


# Script Name:                  ops401_challenge16.py
# Author:                       Michael Roberts 
# Date of latest revision:      01/29/2024
# Purpose:                      create a python script that uses tcp/ip scanning 
# Execution:			        have to run python3 ops401_challenge16.py
# Documentation                 used bard here https://bard.google.com/chat/4efc2c982e36c621



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
        print(f'{lower_answer} is in dict')
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
                    print(f"{line} is in the pass file")
                else:
                    print('string in file is not in pass file')
                # time.sleep(1)    

if __name__ == "__main__":
    listed_words = get_file()
    # print(listed_words)
    passwords = load_ext_file(listed_words)
    load_ext_file(listed_words)
    while True:
        print('option 1:compare string\noption 2:compare string in filepath')
        chk = int(input('option[1] or option[2]? '))
        if chk == int(1):
            check_for_word(passwords)
        elif chk == int(2):
            check_filepath(listed_words)

        like_to_continue = input("would you like to continue checking? ")
        
        if like_to_continue == str('yes') or like_to_continue == str('y'):
            continue
        else:
            break