#!/bin/bash

# Script Name:                  ops-301d14:Challenge2.sh
# Author:                       Michael Roberts 
# Date of latest revision:      11/29/2023
# Purpose:                      modify permission
# Execution:			        bash ops-301d14:Challenge2.sh or ./ops-301d14:Challenge2.sh chmod -x ops-301d14:Challenge2.sh
# Documentation                 Chap-GPT and info was used here https://chat.openai.com/share/0b2fa5cf-0ed4-4eca-bd4a-9bbc00832560

# Before this command i like to create a dir and name it testFolder and file within the folder
# named testFile.txt and then ls -l to show the permissions of the files. The -r interprets / as literals

echo -n "what is the directory path: " && read -r name

echo -n "what permissions numbers (only 000-777) would you like to mod: " && read numbers

cd $name 
chmod $numbers *
# The star is a 'Wildcard' which selects all the files within the folder

ls -l

# after this is done you can rm -rf testFolder to remove it

