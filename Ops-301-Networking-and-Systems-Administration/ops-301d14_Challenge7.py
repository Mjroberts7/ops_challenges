# Import libraries

import os

# Script Name:                  ops-301d14_Challenge7.py
# Author:                       Michael Roberts 
# Date of latest revision:      12/06/2023
# Purpose:                      use python to 
# Execution:			        python3 ops-301d14_Challenge7.py 
# Documentation                 

# created a list of ten string elements
listoften = ['monkey', 'snake', 'elephant', 'dolphin', 'giraffe', 'gorilla', 'dog', 'cat', 'bear', 'deer']

# assigned to a variable the list of string elements
animals = listoften

# printing the 4th element in the list
print(listoften[3])
# printing the 6-10th element in the list
print(listoften[5:10])
# changing the value ofthe 7th element to onion
listoften[6] = 'onion'
print(listoften[6])

# appending walrus to animals
animals.append('walrus')
print(animals)

# copying the animals variable
animals.copy()
print(animals)

# prints how many times monkey is in animals
print(animals.count('monkey'))

# extends the animals list to include the new_animal list
new_animal = ['dragon', 'lizard']
animals.extend(new_animal)
print(animals)

# returns the posititon of the index in new_animal and pops it
new_animal.pop(new_animal.index('lizard'))
print(new_animal)

# inserts an element into the animals list and then reverses the list
animals.insert(1, 'reptilian')
animals.reverse()
print(animals)

# sorts all of animals in the list in alphabetical order
animals.sort()
print(animals)

# removes the word onion from animals because it is not an animal
animals.remove('onion')
print(animals)

# an example of a tuple that uses () and is immutable
tupleExample = ('turtle 1', 'turtle 2', 'turtle 3')
print(tupleExample)

# example of a set that will omit any multi numbers and only display a single number for each element
setExample = {1, 1, 2, 3, 5, 8}
print(setExample)

# dictionary example
dictExample = {
    'Name' : 'Billy Bob',
    'Height' : '4ft',
    'Age' : '53',
    'Time of year' : 'Summer',
    'Time of day' : 'Night',
    'Temp' : 'Hot',
    'Loves' : 'Charlene',
    'Tractor Color' : 'Green',
}
print(dictExample)