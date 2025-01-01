input = open("input10.txt", "r").read()

def LookAndSay(input):
    next = ""
    last = input[0]
    for c in input[1:]:
        if c not in last:
            next += str(len(last)) + last[0]
            last = ''
        last += c
    if(len(last) > 0):
        next += str(len(last)) + last[0]
    return next
copy = input
for i in range(40):
    input = LookAndSay(input)
for i in range(50):
    copy = LookAndSay(copy)
print(len(input))
print(len(copy))
        

