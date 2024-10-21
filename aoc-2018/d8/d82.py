data = open('data', 'r')

data = data.read()

data = data.split()

for i in range(len(data)):
    data[i] = int(data[i])

def read(index):
    childcount = data[index]
    index += 1
    metacount = data[index]
    index += 1

    childvalues = [0]*childcount

    for i in range(childcount):
        index, total = read(index)
        childvalues[i] = total

    total = 0

    for i in range(metacount):
        if childcount > 0:
            mindex = data[index]
            if mindex > 0 and mindex <= childcount:
                total += childvalues[mindex-1]
        else:
            total += data[index]
        index += 1

    return index, total

print(read(0))
