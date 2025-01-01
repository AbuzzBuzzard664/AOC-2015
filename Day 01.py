#Python AOC 2015 Day 1

import re

def GetPuzzleInput():
    with open("input01.txt", "r") as file:
        input = file.read()
        file.close()
    return input

input = GetPuzzleInput()
#Part 1
answer = 0
for c in input:
    if c == '(':
        answer+=1
    else:
        answer-=1
print(answer)

#Part 2
floor = answer = 0 
for i in range(0, len(input)):
    if input[i] == '(':
        floor+=1
    else:
        floor-=1
    
    if floor == -1:
        answer = i+1
        break
print(answer)

