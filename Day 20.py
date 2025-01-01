def GetPuzzleInput():
    with open("input20.txt") as file:
        return file.read().strip()


answer = int(GetPuzzleInput())

# Part 1
temp = 0
i = 0
while temp < answer:
    i += 1
    temp = sum(j * 10 for j in range(1, int(i**0.5) + 1) if i % j == 0 for j in (j, i // j))
    if temp > answer:
        print("Part 1:", i)

# Part 2
temp = 0
i = 0
while temp < answer:
    i += 1
    temp = sum(j * 11 for j in range(1, int(i**0.5) + 1) if i % j == 0 for j in (j, i // j) if i // j <= 50)
    if temp >= answer:
        print("Part 2:", i)

