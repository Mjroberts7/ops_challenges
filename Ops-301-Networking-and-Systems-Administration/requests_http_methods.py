# Import libraries
import os
import requests
import time
# Script Name:                  ops-301d14_Challenge11.py
# Author:                       Michael Roberts 
# Date of latest revision:      12/12/2023
# Purpose:                      utilize requests to print HTTP methods
# Execution:			        python3 ops-301d14_Challenge11.py 
# Documentation                 https://requests.readthedocs.io/en/latest/ , https://chat.openai.com/share/c3a85a6b-af30-4865-9784-e43909b2a4ff

#Instructions { Prompt the user to type a string input as the variable for your destination URL.
urldest = str(input('What url would you like to search? '))

#Prompt the user to select a HTTP Method of the following options. made a list of the options and then a str var to
# pick which one 
listofhttpmethods = ['get', 'post', 'put', 'delete', 'head', 'patch', 'options']
methodprompt = str(input(f'Type which http method would you like to select out of {listofhttpmethods}? '))


def httpmethodsfunc(method, url):
    #GET
    if method.lower() == 'get':
        return requests.get(url)
    #POST
    elif method.lower() == 'post':
        return requests.post(url)
    #PUT
    elif method.lower() == 'put':
        return requests.put(url)   
    #DELETE 
    elif method.lower() == 'delete':
        return requests.delete(url)
    #HEAD    
    elif method.lower() == 'head':
        return requests.head(url) 
    #PATCH   
    elif method.lower() == 'patch':
        return requests.patch(url)
    #OPTIONS 
    elif method.lower() == 'options':
        return requests.options(url)
    else:
        return None

r = requests.get(urldest)

# when response is called the inputs for methodprompt and urldest are plugged into the httpmethodsfunc function and perform a request
response = httpmethodsfunc(methodprompt, urldest)

#Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
print('...')
checker = str(input(f'You are about to send a {methodprompt} request to the url {urldest}, continue? '))

#Using the requests library, perform a request against the destination URL with the HTTP Method selected by the user.
if checker.lower() == 'yes':
    print(response)
else:
    print('invalid input')

#For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#prints None if a there is no error
time.sleep(3)
print(r.raise_for_status())



#For the given URL, print response header information to the screen.
time.sleep(2)
print(r.headers)


 