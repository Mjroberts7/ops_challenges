#powershell script

# Script Name:                  ops10_powershell.ps1
# Author:                       Michael Roberts 
# Date of latest revision:      11/03/2023
# Purpose:                      to output eventlog information from powershell file
# Execution:			        powershell ops10_powershell.sh or ./ops10_powershell.sh chmod -x ops9_powershell.sh
# documentation:                chatgpt https://chat.openai.com/c/d202285f-b812-4dbd-920d-2c951a6fe001

# Declaration of variables

# Declaration of functions



# Main
# prints to the terminal screen all active processes ordered by highest CPU time consumption at the top. 
Get-Process | Sort-Object CPU -Descending
# All active processes ordered by highest Process Identification Number at the top.
Get-Process | Sort-Object ID -Descending
# The top five active processes ordered by highest Working Set (WS(K)) at the top.
Get-Process | Sort-Object WS -Descending
# Start and open browser https://owasp.org/www-project-top-ten/.
Start-Process "https://owasp.org/www-project-top-ten"
# For loop that opens Notepad ten times 
for ($i = 1; $i -le 11; $i++) {
    Notepad.exe
}
# Close each instance of Notepade
$notepad_instance = Get-Process | Where-Object { $_.ProcessName -eq "notepad" }
for ($i in $notepad_instance) {
    Stop-Process -Name "notepad"
}
#Kill a process by its Process Identification Number. Choose a process whose termination won’t destabilize the system, such as Google Chrome or MS Edge.
$notepad_instance = Get-Process | Where-Object { $_.ProcessName -eq "notepad" }
for ($i in $notepad_instance) {
    Stop-Process -ID # whatever ID number Notepad was assigned when it was opened
}
# End