#powershell script

# Script Name:                  ops9_powershell.ps1
# Author:                       Michael Roberts 
# Date of latest revision:      11/02/2023
# Purpose:                      to output eventlog information from powershell file
# Execution:			        powershell ops9_powershell.sh or ./ops9_powershell.sh chmod -x ops9_powershell.sh
# documentation:                chatgpt https://chat.openai.com/c/bef32ea3-a142-4cbd-adfc-d415045bca62

# Declaration of variables

# Declaration of functions



# Main
# This command will output all events from the event log and creates a file called last_24.txt to transfer them to. I created a folder on the desktop name new folder to transfer them to instead    
Get-EventLog -LogName System -After (Get-Date).AddHours(-24) | Out-File -FilePath "C:\Users\mjalm\OneDrive\Desktop\New folder (2)\last_24.txt"
#This command outputs all “error” type events from the System event log to a file within a folder on the desktop named errors.txt.
Get-EventLog -LogName System -EntryType Error | Out-File -FilePath "C:\Users\mjalm\OneDrive\Desktop\New folder (2)\errors.txt"
#This command prints to the screen all events with ID of 16 from the System event log.
Get-EventLog -LogName System | Where-Object { $_.EventID -eq 16 } | Format-Table -Property TimeGenerated, EventID, Message -AutoSize
#This command prints to the screen the most recent 20 entries from the System event log.
Get-EventLog -LogName System -Newest 20
#This command creates a variable that will store the 500 newest Event Log Entries. Then the for loop will print to the screen all sources of the 500 most recent entries in the System event log in full description. 
$500eventLogEntries = Get-EventLog -LogName System -Newest 500
foreach ($entry in $500eventLogEntries) {
    Write-Host "Source: $($entry.Source)"
    Write-Host "Message:"
    Write-Host $entry.Message
    Write-Host "-" * 80  # Separator
}


# End