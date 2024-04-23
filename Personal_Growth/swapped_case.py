#!/usr/bin/env python3

# Author:               Michael Roberts
# Latest Revision:      04/23/2024
# purpose:              to swap the opposite (upper/lower) case for each character in a given string
 
def swap_case(s):
    s2 = ''

    for chr in s:
        if chr.isupper():
            s2 += chr.lower()
        elif chr.islower():
            s2 += chr.upper()
        else:
            print("not doing something right")
    return s2

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)