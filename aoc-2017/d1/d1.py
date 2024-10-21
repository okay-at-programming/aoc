test = ['1122', '1111', '1234', '91212129']
data = [open('data').read().strip()]


for d in data:
    i = 0
    total = 0
    while i+1 < len(d):
        if d[i] == d[i+1]:
            total += int(d[i])
        i += 1
    if d[0] == d[-1]:
        total += int(d[0])
    print(total)
