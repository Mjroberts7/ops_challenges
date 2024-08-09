#!/bin/bash

# Script Name:                  loops_week5.sh
# Author:                       Michael Roberts 
# Date of latest revision:      10/27/2023
# Purpose:                      create a loop to get processes and kill them
# Execution:			        bash loops_week5.sh or ./loops_week5.sh chmod -x loops_week5.sh
# Documentation help            This site helped me write some after i had my idea of how it should go
#                               https://chat.openai.com/c/c00a4e36-a042-430a-a62f-9d76422b6c39
# If you want to make it kill the process uncomment it out the pound signs on 34 and 35
# Declaration of variables
pID=()

# Add the PIDs you want to monitor to the array
pID+=("15")  


while true; do
  # Loop indefinitely

  for id in "${pID[@]}"; do
    # Iterate through the array of PIDs

    # Check if the process with the given PID is running
    if ps -p "$id" > /dev/null; then
      # The process is running, display its details
      echo "Process with PID $id is running:"
      ps aux | grep "$id"
    else
      # The process is not running
      echo "Process with PID $id is not running."
      read -p "Enter a new PID: " newPID
      echo "New PID: $newPID"
      # Uncomment the following line to kill the process
      # kill "$id"
    fi
  done

  # Sleep for some time before checking again (adjust the sleep duration as needed)
  sleep 10
done

# Declaration of functions


#if ps -p "pid" &> /dev/null: then
 #   process_name-$(ps -p "$pid -o comm-)
  #  if [[ "process_name" !- "kernel" ]]

# Main


#while (( id in ${pID[$]} ))
#do
 #   ps aux | grep id 
  #  read $pID
   # echo $pID
    #kill id
#done


# End