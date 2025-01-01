import re

def GetPuzzleInput():
    strings = []
    with open("input05.txt") as file:
       for line in file:
           strings.append(line.removesuffix("\n"))
    file.close()
    return strings

def IsNice1(string):
    if len(re.findall(r"[aeiou]", string)) < 3:
        return False
    elif len(re.findall(r"(ab)|(cd)|(pq)|(xy)", string)) > 0:
        return False
    else:
        last = ''
        for c in string:
            if last == c:
                return True
            last = c
    return False

def IsNice2(string):
    hasDouble = False
    splitDouble = False
    for i in range(1, len(string)-1):
        double = string[i-1] + string[i]
        if double in string[i+1:]:
            hasDouble = True
            break
    for i in range(1, len(string)-1):
        if(string[i-1] == string[i+1]):
            splitDouble = True
            break
    return hasDouble and splitDouble


strings = GetPuzzleInput()
# Part 1
answer = 0
for string in strings:
    answer += int(IsNice1(string))
print(answer)

# Part 2
answer = 0
for string in strings:
    answer += int(IsNice2(string))
print(answer)