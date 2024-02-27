#!/usr/bin/env python3

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests
import os
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
# - Generate a .html file to capture the contents of the HTTP response
# - Open it with Firefox
#
# Stretch Goal
# - Give Cookie Monster hands

# This is where MJ starts on it. 

second_response = requests.get(targetsite, cookies=cookie)

html_file = "fileforcookierequest.html"
# this is one way to output to an html file but if this is giving issues then go to line 54-56
'''
if os.path.exists("fileforcookierequest.html"):
    os.system(f"cat {second_response} > fileforcookierequest.html")
else:
    os.system("touch fileforcookierequest.html")
'''
# this is the second way to create and open a file for the output 
with open(html_file, 'w') as file:
    file.write(second_response)


webbrowser.get("firefox").open("fileforcookierequest.html")

# documentation https://chat.openai.com/share/533525a6-5839-42cd-a5bd-852cad33ce3c