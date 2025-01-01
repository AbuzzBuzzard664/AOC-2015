def check(s):
    if( 'i' in s or 'o' in s or 'l' in s):
        return False
    count = 0
    flag = 0
    char = ""
    for i in range(len(s)-1):
        if(s[i] == s[i+1] and s[i] not in char):
            count += 1
            char += s[i]
    for i in range(len(s)-2):
        if(s[i] == chr(ord(s[i+1])-1) and s[i+1] == chr(ord(s[i+2])-1)):
            flag = 1
    if(count >= 2 and flag == 1):
        return True
    else:
        return False

def gen(s):
    temp = ""
    if ord(s[len(s)-1])-96 == 26:
        temp += gen(s[:len(s)-1]) + "a"
    else:
        return s[:-1] + chr(ord(s[len(s)-1])+1)
    return temp

test = 0
password = open("input11.txt", "r").read().strip()
while not check(password):
    password = gen(password)
print(password)
password = gen(password)
while not check(password):
    password = gen(password)
print(password)