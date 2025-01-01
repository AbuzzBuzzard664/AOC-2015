# Advent Of Code 2015 Day 3
def GetPuzzleInput():
    return open("input03.txt", "r").read()


# Part 1
directions = GetPuzzleInput()
curPos = 0+0j
houses = [curPos]
answer = 1
for direction in directions:
    match direction:
        case '>':
            curPos += 1
        case '<':
            curPos += -1
        case '^': 
            curPos += 1j
        case 'v':
            curPos += -1j
    if not houses.__contains__(curPos):
        answer+=1
        houses.append(curPos)
print(answer)

#Part 2
SantaPos = 0+0j
RoboPos = 0+0j
curPos = 0+0j
houses = [curPos]
answer = 1
i = 0
for direction in directions:
    move = 0+0j
    match direction:
        case '>':
            move += 1
        case '<':
            move += -1
        case '^': 
            move += 1j
        case 'v':
            move += -1j
    if i % 2 == 0:
        SantaPos += move
        curPos = SantaPos
    else:
        RoboPos += move
        curPos = RoboPos
    if not houses.__contains__(curPos):
        answer+=1
        houses.append(curPos)
    i+=1
print(answer)
     