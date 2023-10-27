#!/bin/bash

# Script Name:                  Array_challenge.sh
# Author:                       Michael Roberts 
# Date of latest revision:      10/26/2023
# Purpose:                      make 4 directories that are within an array and reference a text file in them
# Execution:			        bash arrays_challenge.sh or ./arrays_challenge.sh chmod -x arrays_challenge.sh

# Declaration of variables

array1=()

# Declaration of functions

function_name() {
    for (( i=1; i < 5; i++ ));
    do 
        mkdir dir$i
        array1+=(dir$i)
        touch ${array1[i-1]}/textfile.txt
    done
}

# Main 

function_name 

# End
