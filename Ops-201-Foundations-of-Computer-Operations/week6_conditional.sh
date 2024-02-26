#!/bin/bash

# Script Name:                  week6_conditional.sh
# Author:                       Michael Roberts 
# Date of latest revision:      10/30/2023
# Purpose:                      check if file or directory exists. if doesnt, create one and add to array
# Execution:			        bash week6_conditional.sh or ./week6_condtional.sh chmod -x demo.sh
# Documentation                 information for chatGPT is here https://chat.openai.com/c/d43b923f-4575-461d-bd14-fb4cb99b6eea
# Declaration of variables
my_array=()
not_in_array=true
# Declaration of functions
is_dir_or_file_in_list() {
    for element in "$my_array[@]";
    do
        read -p "is this a file or dir: " fileordir

        if [ $fileordir == "file" ]; then
            touch "$dirp.text"
            return 0
        elif [ $fileordir == "dir" ]; then 
            mkdir $dirp
            return 0
        else
            continue
        fi
    done
    return 1
}
while true; 
do
    read -p "File or Dir to check: " dirp

    if [ -z "$dirp" ]; then 
        break
    fi
    
    if [ ! -e "$dirp" ]; then 
        my_array+="$dirp"
        is_dir_or_file_in_list "$dirp"
    fi
done

echo "Final list of inputs"
for element in "${my_array[@]}"; 
do 
    echo "$element" 
done

# Main



# End
    #if  [ -e "$dirp" ]; then
     #   is_dir_or_file_in_list "$dirp"
      #  continue
    #fi