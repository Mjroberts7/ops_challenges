
# Script Name:                  401Lab4.ps1
# Author:                       Michael Roberts 
# Date of latest revision:      01/11/2024
# Purpose:                      powershell script that disables SMB v1 and has some other optional commands 
# Execution:			        powershell 401Lab4.ps1
# Documentation                 Microsoft Documentation https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3?tabs=server#how-to-detect-status-enable-and-disable-smb-protocols-on-the-smb-client


# SMB v1 configuration to disabled
Set-SmbServerConfiguration -EnableSMB1Protocol $false

# Get-Help
# Get-LocalUser
# Get-Command
