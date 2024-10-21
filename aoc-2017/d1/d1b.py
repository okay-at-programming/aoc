test = ['1212', '1221', '123425', '123123', '12131415']
data = [open('data').read().strip()]


for d in data:
    i = 0
    total = 0
    delta = len(d)//2
    while i < len(d):
        j = (i+delta)%len(d)
        if d[i] == d[j]:
            total += int(d[i])
        i += 1
    print(total)
