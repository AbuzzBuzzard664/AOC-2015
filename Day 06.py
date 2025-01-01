import re
def GetPuzzleInput():
    lightsToTurn = []
    with open("input06.txt") as file:
        for line in file:
            if line.startswith("turn on"): 
                turnOn = 1
            elif line.startswith("turn off"): 
                turnOn = 0
            else: 
                turnOn = 2
            positions = re.findall(r"\d+,\d+", line)
            temp = positions[0].split(",")
            x= int(str(temp[0]))
            y = int(str(temp[1]))
            firstPos = complex(x,y)
            temp = positions[1].split(",")
            x= int(str(temp[0]))
            y = int(str(temp[1]))
            secondPos = complex(x,y)
            lightsToTurn.append((firstPos, secondPos, turnOn))
    return lightsToTurn

def Makegrid():
    grid = [[]]
    for i in range(1000):
        grid.append([])
        for _ in range(1000):
            grid[i].append(0)
    return grid

def Calculate(grid):
    answer = 0
    for row in grid:
        for light in row:
            answer += light
    return answer

lightsToTurn = GetPuzzleInput()
# Part 1 & Part 2
grid = Makegrid()
grid2 = Makegrid()
for (firstPos, secondPos, turnOn) in lightsToTurn:
    for y in range(int(firstPos.imag), int(secondPos.imag+1)):
        for x in range(int(firstPos.real), int(secondPos.real+1)):
            match turnOn:
                case 0:
                    grid[y][x] = False
                    if grid2[y][x] is not 0: 
                        grid2[y][x] -= 1
                    
                case 1:
                    grid[y][x] = True
                    grid2[y][x] += 1
                case 2:
                    grid[y][x] = not grid[y][x]
                    grid2[y][x] +=2

print(Calculate(grid))
print(Calculate(grid2))


