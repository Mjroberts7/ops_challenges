# Script Name:                  ops401_challenge1.ps1
# Author:                       Michael Roberts 
# Date of latest revision:      01/08/2024
# Purpose:                      create a powershell script to automate the antivirus software
# Execution:			        run the ops401_challenge1.ps1 file in powershell.
# Documentation                 Chap-GPT and slightly helped here https://chat.openai.com/share/c6d9d381-c178-48ac-a4d0-faaf6a9dba8c 

# The Get-Help command can be used for a multitude of uses 
# The Get-Command command can help with looking up commands used by powershell but for this Get-Help works fine

# Get-Help Set-MpPreference
# This command has all of the commands for setting the antivirus settings on powershell. 

# This command will perform a quick antimalware scan everyday at 1 AM to not disrupt work
Set-MpPreference -ScanParameters QuickScan -ScanScheduleDay Everyday -ScanScheduleTime (Get-Date "01:00")

# This command will perform a full antivirus scan every Friday at 10 PM to not disrupt work as well
Set-MpPreference -ScanParameters FullScan -ScanScheduleDay Friday -ScanScheduleTime (Get-Date "22:00")

# I plan to come back to this to add more but this covers the simplicity of it for now.