#!/bin/bash

# Script Name:                  301OpsChal1.sh
# Author:                       Michael Roberts 
# Date of latest revision:      11/28/2023
# Purpose:                      to create variables and array and append var to array
# Execution:			        bash 301OpsChal1.sh or ./301OpsChal1.sh chmod -x 301OpsChal1.sh
# Documentation                 Chap-GPT and info was used here https://chat.openai.com/share/f3e109b3-6f6b-4eaa-96c6-a00dab0af1f2  https://www.ibm.com/docs/en/aix/7.2?topic=files-copying-cp-command 

mkdir tempFolder
touch tempFile.txt
cp /var/log/syslog tempFile.txt
#just made a folder, file, and copied the contents of the system logs into the file.

#can change the path to whatever folder you want to move it to. 
mv tempFile.txt /home/mjroberts/ops_challenges/tempFolder

currentDate=$(date +"%d-%m-%Y")

echo "Current date: $currentDate"
echo "appending date to file"
echo "current Date: $currentDate" >> tempFile.txt