grid = [[0] * 1000 for i in range(1000)]

for line in open('data1', 'r'):
    claim, at, start, area = line.split()

    splitstart = start.split(',')
    x = int(splitstart[0])
    y = int(splitstart[1][:-1])

    splitarea = area.split('x')
    dx, dy = int(splitarea[0]), int(splitarea[1])

    for i in range(x, x+dx):
        for j in range(y, y+dy):
            grid[i][j] += 1

total = 0
for row in grid:
    for cell in row:
        if cell > 1:
            total += 1

print(total)
