#!/bin/bash

# Script Name:                  ops-301d14:Challenge3.sh
# Author:                       Michael Roberts 
# Date of latest revision:      11/30/2023
# Purpose:                      to create a conditional that prompts for inputs
# Execution:			        bash ops-301d14:Challenge3.sh or ./ops-301d14:Challenge3.sh chmod -x ops-301d14:Challenge3.sh
# Documentation                 Chap-GPT and info was used here 

# Declaration of Variables

echo "say hello? press 1"
echo "ping ?     press 2"
echo "get ip?    press 3"
echo "exit?      press 4"
read -p "what do you want to do: " userinput

while true: do {
    if [ $userinput == 1 ]; then
        echo "Hello world!"
    fi

    if [ $userinput == 2 ]; then
        read -p "what address do you want to ping?" address
        ping $address
    fi

    if [ $userinput == 3 ]; then
        read -p "do you have a windows system, or a linux/mac system?" system
        if [ $system -eq "windows" ]: then
            ipconfig
        else : 
            ip a
            
        fi

    if [ $userinput == 4 ]; then
        echo "Goodbye!"
        break
    fi

    if [ $userinput != 1 ] && [ $userinput != 2 ] && [ $userinput != 3 ] && [ $userinput != 4 ]; then
        echo "that response wont work"
        echo "enter another" 
    fi
}


