
# Author:               Michael Roberts
# Date:                 05/02/2024  
# Purpose:              to change permissions to given paths in powershell

echo 'this scipt is for granting permissions to a certain directory path.'

$directory=Read-host 'What directory would you like to modify permissions for? (include full path C:\) '

$permissions=Read-host 'What is the new permissisons? ' or 'Everyone:(OI)(CI)(R)'

icacls $directory /grant '$permissions'

icacls $directory