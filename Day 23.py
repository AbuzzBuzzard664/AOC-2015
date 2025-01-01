import re

def GetPuzzleInput():
    instructions = []
    with open("input23.txt") as file:
        for line in file:
            splits = re.split(r",? ", line.strip())
            if len(splits) == 2:
                instructions.append((splits[0], splits[1]))
            else:
                instructions.append((splits[0], splits[1], splits[2]))
    return instructions

def CompleteInstructions(instructions, registers):
    i = 0
    while i < len(instructions):
        match instructions[i]:
            case ("hlf", reg):
                registers[reg] //= 2
                i += 1
            case ("tpl", reg):
                registers[reg] *= 3
                i += 1
            case ("inc", reg):
                registers[reg] += 1
                i += 1
            case ("jmp", offset):
                i += int(offset)
            case ("jie", reg, offset):
                if registers[reg] % 2 == 0:
                    i += int(offset)
                else:
                    i += 1
            case ("jio", reg, offset):
                if registers[reg] == 1:
                    i += int(offset)
                else:
                    i += 1
    return registers

instructions = GetPuzzleInput()
# Part 1
print(CompleteInstructions(instructions, {"a": 0, "b": 0})['b'])
# Part 2
print(CompleteInstructions(instructions, {"a": 1, "b": 0})['b'])