indata = [l.strip() for l in open('data')]


grid = set()

r = len(indata)//2


for y in range(len(indata)):
    for x in range(len(indata)):
        if indata[y][x] == '#':
            grid.add((x-r,y-r))


dirs = ((0,-1),(1,0),(0,1),(-1,0))

p = 0,0
d = 0
c = 0

for _ in range(10000):

    if p in grid:
        d = (d+1)%4
        grid.remove(p)
    else:
        d = (d-1)%4
        grid.add(p)
        c += 1

    p = p[0]+dirs[d][0],p[1]+dirs[d][1]


print(c)
