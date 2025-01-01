# Advent Of Code 2015 Day 2

def GetPuzzleInput():
    dimensions = [[]]
    with open("input02.txt", "r") as file:
        i = 0
        for line in file:
            j = 0
            temp =[]
            for x in line.removesuffix("\n").split('x'):
                temp.insert(j, int(x))
                j+=1
            if temp.count != 0:
                dimensions.insert(i, temp)
            i+=1
        file.close()
    dimensions.remove([])
    return dimensions 

dimensions = GetPuzzleInput()
# part 1
answer = 0
for lwh in dimensions:
    if lwh.count != 0:
        a = lwh[0] * lwh[1]
        b = lwh[0] * lwh[2]
        c = lwh[1] * lwh[2]
        answer += 2*a + 2*b + 2*c + min(a, b, c)
print(answer)

# Part 2
answer = 0
volume = 0
for lwh in dimensions:
    volume = lwh[0]*lwh[1]*lwh[2]
    if min(lwh) == lwh[0]:
        if lwh[1] < lwh[2]:
            answer += volume + 2*lwh[0] + 2*lwh[1]
        else:
            answer += volume + 2*lwh[0] + 2*lwh[2]
    elif min(lwh) == lwh[1]:
        if lwh[0] < lwh[2]:
            answer += volume + 2*lwh[1] + 2*lwh[0]
        else:
            answer += volume + 2*lwh[1] + 2*lwh[2]
    else:
        if lwh[0] < lwh[1]:
            answer += volume + 2*lwh[2] + 2*lwh[0]
        else:
            answer += volume + 2*lwh[2] + 2*lwh[1]

print(answer)