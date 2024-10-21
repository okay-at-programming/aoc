best = None

bots = []
ranges = [0 for _ in range(6)]

for line in open('data'):
    s = line.index('<') + 1
    e = line.index('>')
    rind = line.index('r') + 2
    x,y,z = [int(i) for i in line[s:e].split(',')]
    r = int(line[rind:])

    bots.append((r,(x,y,z)))

    if x < ranges[0]:
        ranges[0] = x
    if x > ranges[1]:
        ranges[1] = x
    if y < ranges[2]:
        ranges[2] = y
    if y > ranges[3]:
        ranges[3] = y
    if z < ranges[4]:
        ranges[4] = z
    if z > ranges[5]:
        ranges[5] = z

    if not best or r > best[0]:
        best = (r,(x,y,z))

#grid = [[[0 for _ in range(ranges[4],ranges[5]+1)] for _ in range(ranges[2],ranges[3]+1)] for _ in range(ranges[0],ranges[1]+1)]
grid = {}
c = 0
t = len(bots)

for bot in bots:
    r = bot[0]
    x,y,z = bot[1]

    for dz in range(z-r, z+r+1):
        yr = r-abs(z-dz)
        for dy in range(y-yr, y+yr+1):
            xr = r - abs(z-dz) - abs(y-dy)
            for dx in range(x-xr, x+xr+1):
                grid[(dx,dy,dz)] = grid.get((dx,dy,dz),0) + 1
    c += 1
    print(c,t)

best = (0,(0,0,0))

for point,b in grid.items():
    if b > best[0]:
        best = b,point
        print(best)

print(best)

