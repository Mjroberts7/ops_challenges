#!/bin/bash

# Script Name:                  ops-301d14:Challenge3.sh
# Author:                       Michael Roberts 
# Date of latest revision:      11/30/2023
# Purpose:                      to create a conditional that prompts for inputs
# Execution:			        bash ops-301d14:Challenge3.sh or ./ops-301d14:Challenge3.sh chmod -x ops-301d14:Challenge3.sh
# Documentation                 Chap-GPT and info was used here https://chat.openai.com/share/ed68fe5a-ddc8-468d-810c-76ca595a2c45


question() {
echo "what do you want to do?"
echo

sleep 1

echo "say hello?   press 1"
echo "ping?        press 2"
echo "get ip?      press 3"
echo "exit?        press 4"

read -p "number: " userinput
echo
sleep 1
}

while true; do 
    question 

    if [ $userinput == 1 ]; then
        echo "Hello world!"
        echo 
        sleep 1
    elif [ $userinput == 2 ]; then
        read -p "what address do you want to ping? " address
        timeout 10 ping $address
        echo
    elif [ $userinput == 3 ]; then
        read -p "do you have a windows system, or a linux/mac system? " system
        echo
        sleep 1
        if [ $system == "windows" ]; then
            ipconfig
            echo
            sleep 1
        elif [ $system == "linux" ] || [ $system == "mac" ]; then
            ip a
            echo 
            sleep 1
        else 
            echo "invalid"
            echo
        fi
    elif [ $userinput == 4 ]; then
        echo "Goodbye!"
        exit 0
    else 
        echo "that response wont work"
        echo "enter another" 
        echo 
        sleep 1
    fi
done



