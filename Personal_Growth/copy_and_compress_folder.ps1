# Import-Modules if you need to here

# Script Name:                  copy_and_compress_folder.ps1
# Author:                       Michael Roberts 
# Date of latest revision:      04/19/2024
# Purpose:                      to copy and compress a folder in powershell
# Execution:			        run copy_and_compress_folder.ps1 on powershell

[int]$question1 = Read-Host "would you like to copy and/or compress a 1.) file or 2.) folder? Press 1 or 2"
$fileorfolder = Read-Host "What is the file/folder you would like to copy and/or compress? (include ext)"


if ($question1 == 1) {
    $new_filename = Read-Host "What is the new file(s) name? (exclude ext)"
    Copy-Item -Path "C:\$fileorfolder" -Destination "C:\$new_filename"
    $question2 = Read-Host "Do you want to compress it? (N/y) "
    
    if ($question2.ToLower() == "y") {
        $compresser = @{
            Path = "C:\$new_filename"
            CompressionLevel = "Fastest"
            DestinationPath = "C:\Archives\$new_filename.zip"
        }
        Compress-Archive @compresser
    } else ($question2.ToLower() == "n") {
        Write-Host "complete"
    }
} elseif ($question1 == 2) {
    $new_foldername = Read-Host "What is the new folder name?"
    Copy-Item -Path "C:\$fileorfolder" -Destination "C:\$new_foldername" 
    $question2 = Read-Host "Do you want to compress it? (N/y) "
    
    if ($question2.ToLower() == "y") {
        Compress-Archive -Path "C:\$new_foldername" -Destination "C:\Archives\$new_foldername"
    } else ($question2.ToLower() == "n") {
        Write-Host "complete"
    }
}




