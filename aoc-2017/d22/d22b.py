indata = [l.strip() for l in open('data')]


grid = {}

r = len(indata)//2


for y in range(len(indata)):
    for x in range(len(indata)):
        if indata[y][x] == '#':
            grid[(x-r,y-r)] = '#'


dirs = ((0,-1),(1,0),(0,1),(-1,0))

p = 0,0
d = 0
c = 0

for _ in range(10000000):

    if p not in grid:
        d = (d-1)%4
        grid[p] = 'W'
    elif grid[p] == 'W':
        c += 1
        grid[p] = '#'
    elif grid[p] == '#':
        d = (d+1)%4
        grid[p] = 'F'
    else:
        d = (d+2)%4
        grid.pop(p)

    p = p[0]+dirs[d][0],p[1]+dirs[d][1]


print(c)
