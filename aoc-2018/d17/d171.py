grid = set()

for line in open('test'):
    a,b = line.split(', ')

    c, d = a.split('=')
    e,f = b.split('=')
    g,h = f.split('..')

    for i in range(int(g), int(h)+1):
        p = None
        if c == 'x':
            p = int(d),i
        else:
            p = i, int(d)
        grid.add(p)

minx = None
miny = None
maxx = None
maxy = None

for p in grid:
    if not minx or p[0] < minx:
        minx = p[0]
    if not miny or p[1] < miny:
        miny = p[1]
    if not maxx or p[0] > maxx:
        maxx = p[0]
    if not maxy or p[1] > maxy:
        maxy = p[1]


drips = [(500,0)]
water = set()

while len(drips) > 0:
    x, y = drips.pop(0)

    if (x,y) in water or (x,y) in grid:
        continue

    water.add((x,y))

    if (x,y+1) in grid:
        drips.append((x-1,y))
        drips.append((x+1,y))
        continue

    drips.append((x,y+1))


for y in range(miny, maxy+1):
    s = ''
    for x in range(minx, maxx+1):
        if (x,y) in grid:
            s += '#'
        elif (x,y) in water:
            s += '~'
        else:
            s += ' '

    print(s)
