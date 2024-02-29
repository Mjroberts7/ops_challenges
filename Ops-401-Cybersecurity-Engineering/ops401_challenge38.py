#!/usr/bin/env python3

# Libraries
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Author:                       Abdou Rockikz
# Description:                  XSS detecting with python 
# Date:                         02/28/2024
# Modified by:                  Michael Roberts
# Modified Script Name:         ops401_challenge38.py
# Purpose:                      XSS detecting with python
# Execution:			        have to run python3 ops401_challenge38.py
# Documentation                 


# functions that has a url as a parameter. From that url it searches all the content in the url and parses it into a html document
# From the html data find all searches for and finds data that is a form and returns the data. 
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# this takes the data from the parameter(labeled form to connect the data from get_all_forms function) and provides multitude of actions with it.\
# it creates an empty array, defines action and method variables which are attributes of the form parameter, then creates and empty list called inputs
# from the for loop it defines inputs attributes type and name and appends them to the inputs list. The details array is then updated with the two variables list and returned for the function
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


# function that takes three parameters. assigns two variables target url and inputs with the url parameter(with form details.action attribute) and the form details.inputs attribute
# there is empty data array. A for loop puts value within the input["value"] element if the type element equals text or search. fetchs inputs name and value. and then if conditional
# stats is input name and value are real then the input_name element of data equals input value. Finally a conditional of if the method element of the param form_details equals post, 
# then return a post request with the url and provided data. if not then return a get request with the url and data
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)


# funtion with a url parameter. Assigns the forms variable with what is returned by the get all forms function. prints an f string informs the user how many forms were detected on a specific website
# a javascript command that will cause a XSS-vulnerable field to create an alert prompt and a variable is assigned with the boolean value False. a for loop assigns two variables and has a conditional 
# that prints three lines with information of the alert and changes the is_vulnerable variable to the boolean True. returns the boolean value for the funciton. 
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = requests.get(url, params="<script>alert('XSS-vulnerability');</script>").text ### TODO: Add HTTP and JS code here that will cause a XSS-vulnerable field to create an alert prompt with some text.
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main


# This main all it does is asks for a url that we are going to be testing. This url is going to pass through all of these functions and return
# if there is xss vulnerabilities and alert if there is. It will print the return value of it all since each function is returning parameters for the other functions
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))


# outputs of a positive test
'''    
Enter a URL to test for XSS:https://xss-game.appspot.com/level1/frame
[+] Detected 1 forms on https://xss-game.appspot.com/level1/frame.
[+] XSS Detected on https://xss-game.appspot.com/level1/frame
[*] Form details:
{'action': '',
 'inputs': [{'name': 'query',
             'type': 'text',
             'value': '\n'
                      '<!doctype html>\n'
                      '<html>\n'
                      '  <head>\n'
                      '    <!-- Internal game scripts/styles, mostly boring '
                      'stuff -->\n'
                      '    <script src="/static/game-frame.js"></script>\n'
                      '    <link rel="stylesheet" '
                      'href="/static/game-frame-styles.css" />\n'
                      '  </head>\n'
                      '\n'
                      '  <body id="level1">\n'
                      '    <img src="/static/logos/level1.png">\n'
                      '      <div>\n'
                      '\n'
                      '<form action="" method="GET">\n'
                      '  <input id="query" name="query" value="Enter query '
                      'here..."\n'
                      '    onfocus="this.value=\'\'">\n'
                      '  <input id="button" type="submit" value="Search">\n'
                      '</form>\n'
                      '\n'
                      '    </div>\n'
                      '  </body>\n'
                      '</html>\n'},
            {'name': None, 'type': 'submit'}],
 'method': 'get'}
True
'''
# outputs of a negative test
'''
Enter a URL to test for XSS:http://dvwa.local/login.php
[+] Detected 1 forms on http://dvwa.local/login.php.
False
'''