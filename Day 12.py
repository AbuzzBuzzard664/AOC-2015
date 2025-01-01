import json

input = open("input12.txt", "r").read().strip()

def Sum(input):
    if isinstance(input, int):
        return input
    if isinstance(input, list):
        return sum(Sum(item) for item in input)
    if isinstance(input, dict):
        return sum(Sum(value) for value in input.values())
    return 0

def Sum2(input):
    if isinstance(input, int):
        return input
    if isinstance(input, list):
        return sum(Sum2(item) for item in input)
    if isinstance(input, dict):
        if "red" in input.values():
            return 0
        return sum(Sum2(value) for value in input.values())
    return 0

data = json.loads(input)
print(Sum(data))
print(Sum2(data))