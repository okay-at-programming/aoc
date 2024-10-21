data = []

for line in open('test', 'r'):
    data.append(line.strip())

length = len(data[0])

for i in range(length):
    for d1 in data:
        for d2 in data:
            if d1 == d2:
                continue
            if d1[:i] + d1[i+1:] == d2[:i] + d2[i+1:]:
                print(d1[:i] + d1[i+1:])

