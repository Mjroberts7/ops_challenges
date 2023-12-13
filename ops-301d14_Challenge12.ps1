# Import libraries
Import-Module  ActiveDirectory
# Script Name:                  ops-301d14_Challenge12.ps1
# Author:                       Michael Roberts 
# Date of latest revision:      12/13/2023
# Purpose:                      to add new user in AD
# Execution:			        run ops-301d14_Challenge12.ps1 on powershell 
# Documentation                 https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps 

#create a new user in AD with automation in powershell
$fullName="Franz Ferdinand"
$firstName="Franz"
$lastName="Ferdinand"

$franzUser = @{
    -Name = $fullName 
    -SamAccountName "ferdi" 
    -UserPrincipalName "ferdi@GlobeXpower.com" 
    -DisplayName $fullName 
    -GivenName $firstName 
    -Surname $lastName 
    -OtherAttributes @{
        'title'="TPS Reporting Lead";'department'="TPS Department";'mail'="ferdi@GlobeXpower.com"
    } 
    -City "Springfield" 
    -State "Oregon" 
    -AccountPassword (ConvertTo-SecureString -AsPlainText "Solarwinds123" -Force) 
    -Enabled $true
}

New-ADUser @$franzUser

