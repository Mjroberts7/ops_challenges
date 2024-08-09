import os
import time

# Script Name:                  ops-301d14_Challenge5.py
# Author:                       Michael Roberts 
# Date of latest revision:      12/04/2023
# Purpose:                      to utilize python to run some script
# Execution:			        python ops-301d14_Challenge5.py or ./ops-301d14_Challenge5.py chmod -x ops-301d14_Challenge5.py
# documentation                 didnt use much help but am always putting it to save my butt https://chat.openai.com/share/56bc1a90-3e52-4779-9c82-9dc120f50030 

# Bash in python 

userInput = input('do you want to run some bash commands? ')


while userInput.upper() == 'Y':

    time.sleep(1)
    print('Would you rather run\n 1. whoami\n 2. ip a\n 3. lshw -short')
    secondUserInput = int(input())

    if secondUserInput == 1:
        time.sleep(1)
        os.system('whoami')
    elif secondUserInput == 2:
        time.sleep(1)
        os.system('ip a')
    elif secondUserInput == 3:
        time.sleep(1)
        os.system('lshw -short')
    else:
        time.sleep(1)
        print('invalid input\nplease input 1-3')
        continue

    stopper = input('Want to run another command? Y/N? ')
    
    if stopper.lower() == 'y':
        continue
    elif stopper.lower() == 'n': 
        userInput = 'n'
    else:
        print('invalid option')


else:
    print(f'Adios!')          
    