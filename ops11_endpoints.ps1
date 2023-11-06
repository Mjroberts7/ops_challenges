#powershell script

# Script Name:                  ops11_endpoints.ps1
# Author:                       Michael Roberts 
# Date of latest revision:      11/06/2023
# Purpose:                      a collection of powershell commands to enable/disable settings. 
# Execution:			        powershell ops11_endpoints.sh or ./ops11_endpoints.sh chmod -x ops11_endpoints.sh
# documentation:                the github repo https://github.com/superswan/Powershell-SysAdmin

# Declaration of variables

# Declaration of functions



# Main
# Enabling file and printer sharing 
Set-NetFirewallRule -DisplayGroup "File And Printer Sharing" -Enabled True
# Allowing ICMP traffic. This allows the IP of another comp to ping through the firewall in. 
netsh advfirewall firewall add rule name="Allow incoming ping requests IPv4" dir=in action=allow protocol=icmpv4 
# Enabling remote management- 
## This command enables remote desktop connection by going to the key in the windows registry and setting the value to 0.
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
## This command is looking into the registry also going into a different key. the key RDP-Tcp and changing the value for UserAuthentication to 1
Set-ItemProperty ‘HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp\‘ -Name “UserAuthentication” -Value 1
## This command alters your firewall from the displayed group name "DisplayGroup" to allow remote desktop access. 
Enable-NetFirewallRule -DisplayGroup “Remote Desktop”
# Removing bloatware from the computer. This is using git and the string debloat from git.io to find and remove the bloatware from the web client. 
iex ((New-Object System.Net.WebClient).DownloadString('https://git.io/debloat'))
# Enabling Hyper-V. This command is enabling an optional feature on windows using the web and the keyword "Microsoft-Hyper-V" and the all is all of the bundle. 
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
# Disabling the SMBv1. This command is pretty self explanitory. It shows the first part is the parameters for SMB configuration. The second part is the key of Enabling SMB. The last part is showing the value to be false. Effectively making Enable SMB to be false and disabling it. 
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force
#End