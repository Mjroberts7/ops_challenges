#!/bin/bash

# Script Name:                  ops-301d14:Challenge2.sh
# Author:                       Michael Roberts 
# Date of latest revision:      11/29/2023
# Purpose:                      modify permission
# Execution:			        bash ops-301d14:Challenge2.sh or ./ops-301d14:Challenge2.sh chmod -x ops-301d14:Challenge2.sh
# Documentation                 Chap-GPT and info was used here https://chat.openai.com/share/0b2fa5cf-0ed4-4eca-bd4a-9bbc00832560

echo "what is the directory path: " && read name

echo "what permissions numbers (only 000-777) would you like to mod: " && read numbers

cd $name 
chmod $numbers

ls -al