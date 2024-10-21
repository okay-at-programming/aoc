grid = [[0] * 1000 for i in range(1000)]

filename = 'data1'

for line in open(filename, 'r'):
    claim, at, start, area = line.split()

    splitstart = start.split(',')
    x = int(splitstart[0])
    y = int(splitstart[1][:-1])

    splitarea = area.split('x')
    dx, dy = int(splitarea[0]), int(splitarea[1])

    for i in range(x, x+dx):
        for j in range(y, y+dy):
            grid[i][j] += 1

for line in open(filename, 'r'):
    claim, at, start, area = line.split()

    splitstart = start.split(',')
    x = int(splitstart[0])
    y = int(splitstart[1][:-1])

    splitarea = area.split('x')
    dx, dy = int(splitarea[0]), int(splitarea[1])

    found = True

    for i in range(x, x+dx):
        for j in range(y, y+dy):
            if grid[i][j] > 1:
                found = False

    if found:
        print(claim)


