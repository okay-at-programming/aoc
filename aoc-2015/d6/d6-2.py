grid = [[0 for _ in range(1000)] for _ in range(1000)]

#for l in ('turn on 0,0 through 999,999','toggle 0,0 through 999,0','turn off 499,499 through 500,500'):
for l in open('data'):
    togg = l.split()[0] == 'toggle'
    on = l.split()[1] == 'on'

    ls = l.split(',')
    x1,y1 = int(ls[0].split()[-1]),int(ls[1].split()[0])
    x2,y2 = int(ls[1].split()[-1]),int(ls[2].split()[0])

    if togg:
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                grid[j][i] += 2
    elif on:
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                grid[j][i] += 1
    else:
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                grid[j][i] = max(0, grid[j][i]-1)

s = 0
for r in grid:
    for c in r:
        s += c

print(s)


