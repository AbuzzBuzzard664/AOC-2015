from itertools import combinations

def GetPuzzleInput():
    packages = []
    with open("input24.txt") as file:
        for line in file:
            packages.append(int(line.strip()))
    return packages

def FindBestGroup(packages, numGroups):
    targetWeight = sum(packages) // numGroups
    for i in range(1, len(packages)):
        for group in combinations(packages, i):
            if sum(group) == targetWeight:
                return group

def CalculateQE(group):
    qe = 1
    for package in group:
        qe *= package
    return qe

packages = GetPuzzleInput()
print(CalculateQE(FindBestGroup(packages, 3)))
print(CalculateQE(FindBestGroup(packages, 4)))