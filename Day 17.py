from itertools import combinations

def GetPuzzleInput():
    bins = []
    with open("input17.txt") as file:
        for line in file:
            bins.append(int(line))
    return bins

def GetCombos(bins):
    target = 150
    all_combos = []
    for i in range(1, len(bins) + 1):
        for combo in combinations(bins, i):
            if sum(combo) == target:
                all_combos.append(combo)
    return all_combos

bins = GetPuzzleInput()
combos = GetCombos(bins)
print(len(combos))

leastbins = float("inf")
for combo in combos:
    leastbins = min(leastbins, len(combo))

answer = 0
for combo in combos:
    if len(combo) == leastbins:
        answer += 1
print(answer)