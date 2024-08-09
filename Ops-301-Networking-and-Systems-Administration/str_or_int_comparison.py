# Import libraries
import time

# Script Name:                  ops-301d14_Challenge8.py
# Author:                       Michael Roberts 
# Date of latest revision:      12/07/2023
# Purpose:                      use python to do some conditional statements
# Execution:			        python3 ops-301d14_Challenge8.py 
# Documentation                 

while True: 
    question = input('would you like to compare a int or str? ')
    if question == 'int' or question == 'str':
        answer = 1
    else:
        print(f'{question} is not an answer, goodbye')
        break

    while answer == 1:
        try:
            inputa = int(input('what is the first number? '))
            print('...')
            inputb = int(input('what is the second number? '))
            print('...')
            time.sleep(1)
        except ValueError:
            print('that dont work')
            break 

        if inputa <= inputb:
            print(f'{inputa} is less than or equal to {inputb}')
            if inputa < inputb: 
                print(f'{inputa} is less than {inputb}')
                if inputa < 5:
                    print('those are rookie numbers\n need to pump them up')
        elif inputa >= inputb:
            print(f'{inputa} is greater than or equal to {inputb}')
            if inputa > inputb:
                print(f'{inputa} is greater than {inputb}')
        else:
            print('invalid input')
            break
    

    while answer == 1:
    
        inputa = str(input('what is the first word? '))
        print('...')
        inputb = str(input('what is the second word? '))
        print('...')
        time.sleep(1)

        
        if inputa == inputb:
            print(f'{inputa} and {inputb} are the same')
            if inputa == 'beer' and inputb == 'beer':
                print('Cheers!')    
            
        if inputa == 'whiskey' or inputb == 'wine':
            print('Classy')

        if inputa != inputb:
            print(f'{inputa} and {inputb} are not the same')
        
        wannacontinue = input('wanna continue? ')
        if wannacontinue == 'no' or wannacontinue == 'NO' or wannacontinue == 'N' or wannacontinue == 'No' or wannacontinue == 'n': 
            break       
    
 
