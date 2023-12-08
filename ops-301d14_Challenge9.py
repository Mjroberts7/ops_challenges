# Import libraries
import os

# Script Name:                  ops-301d14_Challenge9.py
# Author:                       Michael Roberts 
# Date of latest revision:      12/08/2023
# Purpose:                      use python to create new .txtfile. appends three lines and prints to the screen the first line then deletes the text file
# Execution:			        python3 ops-301d14_Challenge8.py 
# Documentation                 https://www.freecodecamp.org/news/file-handling-in-python/ 

# creates a new file with python. x creates the file. 
nf = 'test_file.txt'

# created a variable to automate the three lines
lines = 'test_file'  

# writing a line of code in the file. 
with open(nf, 'w') as new:
    new.write(f'{lines}1 \n')
    
# appending three lines of code to the file
with open(nf, 'a') as new:
    new.write(f'{lines}2 \n')
    new.write(f'{lines}3 \n')
    new.write(f'{lines}4 \n')

with open(nf, 'r') as new:
    for line in new:
        if '1' in line:
            print('First line: ', line)

new.close()
        
os.remove('test_file.txt')