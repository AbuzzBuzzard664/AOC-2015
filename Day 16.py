items = set()

def GetPuzzleInput():
    aunts = []
    with open("input16.txt") as file:
        for line in file:
            splits = line.strip().split(" ")
            temp = {}
            i = 2
            while i in range(2, len(splits)):
                temp[splits[i][:-1]] = int(splits[i+1].removesuffix(","))
                items.add(splits[i][:-1])
                i+=2
            aunts.append(temp)
    file.close()
    return aunts
                                
aunts = GetPuzzleInput()
values = {"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1}

for aunt in aunts:
    isAunt = True
    for items, amounts in aunt.items():
        if values[items] is not amounts:
            isAunt = False
    if isAunt:
        print(aunts.index(aunt)+1)

for aunt in aunts:
    isAunt = True
    for items, amounts in aunt.items():
        match items:
            case "cats" | "trees":
                if not values[items] < amounts:
                    isAunt = False
            case "pomeranians" | "goldfish":
                if not values[items] > amounts:
                    isAunt = False
            case _:
                if values[items] != amounts:
                    isAunt = False
    if isAunt:
        print(aunts.index(aunt)+1)