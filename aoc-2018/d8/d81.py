data = open('data', 'r')

data = data.read()

data = data.split()

for i in range(len(data)):
    data[i] = int(data[i])

def read(index, total):
    childcount = data[index]
    index += 1
    metacount = data[index]
    index += 1

    for i in range(childcount):
        index, total = read(index, total)

    for i in range(metacount):
        total += data[index]
        index += 1

    return index, total

print(read(0, 0))
