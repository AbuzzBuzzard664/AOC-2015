from itertools import permutations

def GetPuzzleInput():
    people = set()
    happiness = {}
    with open("input13.txt") as file:
        for line in file:
            person, _, gainlose, amount, _, _, _, _, _, _, neighbor = line.strip().split()
            people.add(person)
            if person not in happiness:
                happiness[person] = {}
            if(gainlose == "lose"):
                amount = "-" + amount
            happiness[person][neighbor.strip('.')] = int(amount) 
    return people, happiness


def GetHappiness(people, happiness):
    maxhappiness = 0
    for perm in permutations(people):
        curHappiness = 0
        for i in range(len(perm)):
            curHappiness += happiness[perm[i]][perm[i-1]]
            curHappiness += happiness[perm[i]][perm[(i+1) % len(perm)]]
        maxhappiness = max(curHappiness, maxhappiness)
    return maxhappiness

people, happiness = GetPuzzleInput()
print(GetHappiness(people, happiness))

people.add("Me")
happiness["Me"] = {}
for person in people:
    happiness["Me"][person] = 0
    happiness[person]["Me"] = 0
print(GetHappiness(people, happiness))