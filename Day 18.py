corners = [1+1j,100+1j,1+100j,100+100j]

def GetPuzzleInput():
    grid = []
    grid.append([])
    for _ in range(102):
        grid[0].append(".")
    with open("input18.txt") as file:
        for line in file:
            grid.append(["."])
            for char in line.strip():
                grid[-1].append(char)
            grid[-1].append(".")
    grid.append([])
    for _ in range(102):
        grid[-1].append(".")
    return grid

def GetNeighbors(grid, point):
    neighbors = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == y == 0:
                continue
            neighbors.append(complex(point.real + x, point.imag + y))
    return neighbors

def Step(grid, point):
    neighbors = GetNeighbors(grid, point)
    on = 0
    for neighbor in neighbors:
        if grid[int(neighbor.real)][int(neighbor.imag)] == '#':
            on += 1
    if grid[int(point.real)][int(point.imag)] == '#':
        if on == 2 or on == 3:
            return '#'
        else:
            return '.'
    else:
        if on == 3:
            return '#'
        else:
            return '.'

def NextGrid(grid):
    new_grid = [row[:] for row in grid]
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[x]) - 1):
            new_grid[x][y] = Step(grid, complex(x, y))
    return new_grid

def NextGrid2(grid):
    new_grid = [row[:] for row in grid]
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[x]) - 1):
            if complex(x,y) in corners:
                continue
            new_grid[x][y] = Step(grid, complex(x, y))
    return new_grid


grid = GetPuzzleInput()
grid2 = GetPuzzleInput()
grid2[1][1] = '#'
grid2[100][1] = '#'
grid2[1][100] = '#'
grid2[100][100] = '#'
for _ in range(100):
    grid = NextGrid(grid)
    grid2 = NextGrid2(grid2)

res = 0
for line in grid:
    res += line.count('#')
print(res)
res = 0
for line in grid2:
    res += line.count('#')
print(res)