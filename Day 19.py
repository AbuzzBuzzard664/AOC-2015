replacements = {}
def GetPuzzleInput():
    with open("input19.txt") as file:
        for line in file:
            if " => " in line:
                splits = line.strip().split(" => ")
                if splits[0] in replacements.keys():
                    replacements[splits[0]].append(splits[1])
                else:
                    replacements[splits[0]] = [splits[1]]
            else:
                startString = line.strip()
    return startString

def GetReplacements(string):
    combinations = set()
    for key, values in replacements.items():
        for i in range(len(string)):
            if string[i:i+len(key)] == key:
                for value in values:
                    temp = string[:i] + value + string[i+len(key):]
                    combinations.add(temp)
    return len(combinations)

numofReplacements = set()

molecule = GetPuzzleInput()
print(GetReplacements(molecule))
reps = []
for key, values in replacements.items():
    for value in values:
        reps.append((key, value))

from random import shuffle

target = molecule
answer = 0
while target != 'e':
    temp = target
    for a, b in reps:
        if b not in target:
            continue
        target = target.replace(b, a, 1)
        answer += 1
    if temp == target:
        target = molecule
        answer = 0
        shuffle(reps)

print(answer)