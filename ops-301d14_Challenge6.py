#!/usr/bin/env python3

# Import libraries

import os

# Script Name:                  ops-301d14_Challenge6.py
# Author:                       Michael Roberts 
# Date of latest revision:      12/05/2023
# Purpose:                      to utilize python to create directories
# Execution:			        python3 ops-301d14_Challenge6.py 
# documentation                 


# Declaration of variables
inputDir = str(input('what do you want the new dir to be? '))
os.makedirs(inputDir)
### Read user input here into a variable # input the inputDir
userinput = str(input('what is the path to the dir to check? '))
# Declaration of functions

    

### Declare a function here
def pyFunction(testdir):
    for (root, dirs, files) in os.walk(testdir):
        ### Add a print command here to print ==root==
        print(root)
        ### Add a print command here to print ==dirs==
        print(dirs)
        ### Add a print command here to print ==files==
        print(files)

# Main

### Pass the variable into the function here
pyFunction(userinput)
# End
# got rid of the test directory after i checked it
os.rmdir(inputDir)