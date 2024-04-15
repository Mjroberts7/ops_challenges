#!/usr/bin/env python3

# Author:           Michael Roberts
# Date:             

# this code returns the sum of three numbers given in a list specific to the queried name. 
# example stdin would look like 
# 2
# mike 25 25 25 
# nigel 98 70 30 
# nigel
# and stdout would show 66.00

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    if query_name in student_marks:
        
        scores = student_marks[query_name]

        a = sum(scores) / 3
        
        print(f'{a:.2f}')