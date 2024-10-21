data = 289326

grid = {(0,0):1}

i = 2
si = 0
sl = 2
sc = 0
pos = (1,0)
dirs = ((0,1),(-1,0),(0,-1),(1,0))
d = 0

while True:
    s = sum([grid.get((pos[0]+adj[0],pos[1]+adj[1]),0) for adj in ((1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1))])
    grid[pos] = s

    if s > data:
        print(s)
        break

    i += 1
    si += 1
    if si == sl:
        sc += 1
        si = 0
        d = (d+1)%4
    if sc == 4:
        sl += 2
        sc = 0
        si = 0
        pos = pos[0]+1,pos[1]
    else:
        pos = pos[0]+dirs[d][0], pos[1]+dirs[d][1]
    print(i,pos)



