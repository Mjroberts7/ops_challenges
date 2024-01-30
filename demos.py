#!/usr/bin/env python3

import nltk
from nltk.corpus import words




def get_word():
    nltk.download('words')
    word_list = words.words()
    return word_list

def check_for_word(words):
    user_answer = input('Enter a word: ')
    lower_answer = user_answer.islower()
    if lower_answer in words:
        print('word is in dict')
    else:
        print('word not in dict')

def load_ext_file():
    password_list = []
    with open('rockyou_sample.txt', 'r') as file:
        line = file.readline()
        if not line:
            break
        line = line.rstrip()
        password_list.append(line)
        print(password_list)


if __name__ == "__main__":
    listed_words = get_word()
    # print(listed_words)
    # check_for_word(listed_words)
    load_ext_file()