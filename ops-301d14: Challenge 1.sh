#!/bin/bash

# Script Name:                  301OpsChal1.sh
# Author:                       Michael Roberts 
# Date of latest revision:      11/28/2023
# Purpose:                      to create variables and array and append var to array
# Execution:			        bash 301OpsChal1.sh or ./301OpsChal1.sh chmod -x 301OpsChal1.sh
# Documentation                 Chap-GPT was used here 


echo ${date}
# Declaration of variables

year=${date +%Y}
echo $year

month=${date +%m}
echo $month

echo "Current date: $day-$month-$year"
echo "append to file"
echo "current Date: $day-$month-$year" >> test.txt