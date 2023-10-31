#!/bin/bash

# Script Name:                  ops7.sh
# Author:                       Michael Roberts 
# Date of latest revision:      10/31/2023
# Purpose:                      to use lshw to grep information from our system components
# Execution:			        bash ops7.sh or ./ops7.sh chmod -x ops7.sh
# Documentation                 information for chatGPT is here https://chat.openai.com/c/2ee6eabe-fdd9-4614-b4a9-c6c2078f5547


# Declaration of variables
my_array=()


# Declaration of functions
put_elemenent_in_array() {
    local new_element="$1"
    for element in $(lshw | grep "$new_element"); do
        my_array+=("$element")
    done
}

# Main
while true; do 
    read -p "Want to look up component? (Type 'true' to continue, 'exit' to quit): " component

    if [ "$component" = "exit" ]; then
        break
    elif [ "$component" = "true" ]; then
        read -p "Enter the component you want to add: " new_component
        put_elemenent_in_array "$new_component"
    else
        echo "Invalid. type 'true' to add a component of 'exit' to quit."
    fi
done 

#The Display of all of the elements in array
echo "Components Displayed"
for element in "${my_array[@]}"; do
    echo "$element"
done
# End