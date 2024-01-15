


# Script Name:                  filehashing.ps1
# Author:                       Michael Roberts 
# Date of latest revision:      01/15/2024
# Purpose:                      powershell script writes a string to a new temp file, gets the hash and then deletes the file simulating the hash of a string 
# Execution:			        powershell filehashing.ps1
# Documentation                 Microsoft Documentation https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-7.4


$tempfile = New-TemporaryFile
$hashstring = Read-Host "What string would you like to get the hash of?"
echo "$hashstring" > $tempfile
Get-FileHash -Path $tempfile | Format-List 
rm $tempfile