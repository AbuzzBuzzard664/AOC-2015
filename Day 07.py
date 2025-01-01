results = dict()

def GetPuzzleInput(operations):
    with open("input07.txt") as file:
        for line in file:
            (ops, res) = line.split('->')
            operations[res.strip()] = ops.strip().split(' ')
    return operations


def Calculate(string):
    try:
        return int(string)
    except ValueError:
        pass

    if string not in results:
        ops = operations[string]
        if len(ops) == 1:
            res = Calculate(ops[0])
        else:
            op = ops[-2]
            match op:
                case "AND":
                    res = Calculate(ops[0]) & Calculate(ops[2])
                case "OR":
                    res = Calculate(ops[0]) | Calculate(ops[2])
                case "NOT":
                    res = ~Calculate(ops[1])
                case "RSHIFT":
                    res = Calculate(ops[0]) >> Calculate(ops[2])
                case "LSHIFT":
                    res = Calculate(ops[0]) << Calculate(ops[2])
        results[string] = res
    return results[string]
# Part 1
operations = dict()
GetPuzzleInput(operations)
answer = Calculate("a")
print(answer)

# Part 2
operations = dict()
GetPuzzleInput(operations)
results.clear()
results["b"]= answer
print(Calculate("a"))