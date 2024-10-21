inst = [int(x) for x in open('data')]

s = 0
i = 0
while i < len(inst):
    d = inst[i]
    if d >= 3:
        inst[i] -= 1
    else:
        inst[i] += 1
    i += d
    s += 1
print(s)
