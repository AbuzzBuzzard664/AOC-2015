import re
def GetPuzzleInput():
    with open("input25.txt") as file:
        nums = re.findall(r"\d+", file.read())
        return int(nums[0]), int(nums[1])
    
def GetCodeNumber(row, col):
    code = 20151125
    for i in range(1, (row + col - 2) * (row + col - 1) // 2 + col):
        code = code * 252533 % 33554393
    return code

row, col = GetPuzzleInput()
print(GetCodeNumber(row, col))