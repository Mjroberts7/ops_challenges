# Import libraries


# Script Name:                  ops-301d14_Challenge8.py
# Author:                       Michael Roberts 
# Date of latest revision:      12/07/2023
# Purpose:                      use python to do some conditional statements
# Execution:			        python3 ops-301d14_Challenge8.py 
# Documentation                 

question = input('would you like to compare a int or str? ')


while question == 'int':

    inputa = int(input('what is the first number? '))
    inputb = int(input('what is the second number? '))


    if inputa < inputb: 
        print(f'{inputa} is less than {inputb}')
        if inputa < 5:
            print('those are rookie numbers\n need to pump them up')
        elif inputa <= inputb:
            print(f'{inputa} is less than or equal to {inputb}')
    elif inputa > inputb:
        print(f'{inputa} is greater than {inputb}')
        if inputa >= inputb:
            print(f'{inputa} is greater than or equal to {inputb}')
    else:
        print('invalid input')
        break
done

while question == 'str':
    
    inputa = str(input('what is the first word? '))
    inputb = str(input('what is the second word? '))

    if inputa == inputb:
        print(f'{inputa} and {inputb} are the same')
    
    if inputa != inputb:
        print(f'{inputa} and {inputb} are not the same')
        continuation = input('do you want to keep going? ')
        if continuation == 'N' or continuation == 'No' or continuation =='no' or continuation == 'n':
            break
        else:
            continue

    if inputa == 'whiskey' or inputb == 'wine':
        print('Classy')
    elif inputa == 'beer' and inputb == 'beer':
        print('Cheers!')    
done
        
