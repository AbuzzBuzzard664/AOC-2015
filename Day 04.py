import hashlib

def GetPuzzleInput():
    with open("input04.txt") as file:
        return file.read().strip()
    
def MD5Hash(string):
    return hashlib.md5(string.encode()).hexdigest()

input = GetPuzzleInput()
# Part 1
i = 0
while not MD5Hash(input + str(i)).startswith("00000"):
    i += 1
print(i)

# Part 2
i = 0
while not MD5Hash(input + str(i)).startswith("000000"):
    i += 1
print(i)