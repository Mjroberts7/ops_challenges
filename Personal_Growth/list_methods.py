#!/usr/bin/env python3

# Author:           Michael roberts
# Date:             04/16/2024


# This is a class for list operations 
class ListOperations:
        def __init__(self):
            self.lst = [] 
    
        def insert(self, idx, value):
            self.lst.insert(idx, value)
        
        def remove(self, value):
            self.lst.remove(value)
        
        def append(self, value):
            self.lst.append(value)
        
        def sort(self):
            self.lst.sort()
        
        def pop(self):
            self.lst.pop()
        
        def reverse(self):
            self.lst.reverse()
        
        def execute_command(self, command, *args):
            if hasattr(self, command):
                getattr(self, command)(*args)
            else:
                print("command not recognized")
        
if __name__ == '__main__':
    n = int(input())
    
    operations = ListOperations()
    
    # Reads each line inputed according to n and executes the commands you choose by calling the ListOperations class
    for line in range(n):
        line = str(input()).strip()
        line = line.split()
        command = line[0]
        args = list(map(int, line[1:]))

        # For each time print is inputed, the outputted list will be printed on a new line.
        if command == 'print':
            print(operations.lst)
        else:
            operations.execute_command(command, *args)
    
    # These are the commands that you can put within the input after you input an int that tells you how many commands to run
    '''
    insert i e: Insert integer at position e
    print: Print the list.
    remove e: Delete the first occurrence of integer e
    append e: Insert integer at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list.
    '''
