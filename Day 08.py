def GetPuzzleInput():
    strings = []
    with open("input08.txt") as file:
        for line in file:
            strings.append(line.strip())
    return strings

def Encode(string : str):
    return '"' + string.replace('\\', '\\\\').replace('"', '\\"') + '"'

strings = GetPuzzleInput()
totalCodeLength = 0
totalMemoryLength = 0
totalEncodedLength = 0
for line in strings:
    totalCodeLength += len(line)
    totalMemoryLength += len(eval(line))
    totalEncodedLength += len(Encode(line))
res = totalCodeLength - totalMemoryLength
print(res)
res = totalEncodedLength - totalCodeLength
print(res)