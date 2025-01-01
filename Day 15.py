def GetPuzzleInput():
    with open("input15.txt") as file:
        for line in file:
            var,_, capacity, _, durability, _, flavor, _, texture, _, calories = line.strip().split(" ")
            yield (var , int(capacity[:-1]), int(durability[:-1]), int(flavor[:-1]), int(texture[:-1]), int(calories))

def GetCombinations(ingredients, total):
    if len(ingredients) == 1:
        yield (total,)
    else:
        for i in range(total+1):
            for result in GetCombinations(ingredients[1:], total-i):
                yield (i,) + result


def GetScore(ingredients, combination):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for i in range(len(ingredients)):
        capacity += ingredients[i][1] * combination[i]
        durability += ingredients[i][2] * combination[i]
        flavor += ingredients[i][3] * combination[i]
        texture += ingredients[i][4] * combination[i]
    return max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)

def GetCalScore(ingredients, combination):
    calories = 0
    for i in range(len(ingredients)):
        calories += ingredients[i][5] * combination[i]
    if calories == 500:
        return GetScore(ingredients, combination)
    else:
        return 0

ingredients = list(GetPuzzleInput())
maxScore = 0
maxCalScore = 0
for combination in GetCombinations(ingredients, 100):
    maxScore = max(maxScore, GetScore(ingredients, combination))
    maxCalScore = max(maxCalScore, GetCalScore(ingredients, combination))
print(maxScore)
print(maxCalScore)