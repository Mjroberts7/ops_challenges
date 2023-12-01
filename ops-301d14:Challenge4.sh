#!/bin/bash


# Script Name:                  ops-301d14:Challenge4.sh.sh
# Author:                       Michael Roberts 
# Date of latest revision:      12/01/2023
# Purpose:                      compress log files give them time stamp. clear the contents of log file and print to the screen the file size of compressed file, the compare size.
# Execution:			        bash ops-301d14:Challenge4.sh or ./ops-301d14:Challenge4.sh.sh chmod -x ops-301d14:Challenge4.sh.sh
# Documentation                 Chap-GPT and info was used here https://chat.openai.com/share/bac510ff-a776-44a1-931d-833726e24da3 

syslogVar="/var/log/syslog"
wtmpVar="/var/log/wtmp"

# Stores both files in single variable
bothFiles="${syslogVar} ${wtmpVar}"
# prints the size of both files
du -h $bothFiles

# put current date and time in variable
currentDate="$(date +%Y-%m-%d-%H-%M-%S)"

# made a dir and compressed the files to the dir with current date added to file name
mkdir tempDir
gzip -c $bothFiles > "tempDir/${currentDate}_bothFiles.zip"

#showing the completed zipped file transfer
sleep 3
du -h tempDir

# clearing the contents of all the files in the directory while keeping the files themselves.
# i would uncomment which ever one i wanted to delete 
#truncate -s 0 tempDir/*
#truncate -s 0 /var/log/syslog
#truncate -s 0 /var/log/wtmp

#sleep 3
#du -h tempDir





