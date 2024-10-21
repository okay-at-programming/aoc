g = set()
m = []
done = False
y = 0

for l in open('data'):
    if done:
        x = 0
        for c in l.strip():
            if c == '#':
                g.add((x,y))
            x += 1
        y += 1
        continue
    elif not l.strip():
        done = True
    else:
        for c in l.strip():
            if c == '#':
                m.append(1)
            elif c == '.':
                m.append(0)
            else:
                assert False

zeroflip = m[0] == 1
ogon = False

for _ in range(50):
    minx = min([x for (x,y) in g])
    miny = min([y for (x,y) in g])
    maxx = max([x for (x,y) in g])
    maxy = max([y for (x,y) in g])

    ng = set()

    for x in range(minx-1,maxx+2):
        for y in range(miny-1,maxy+2):
            i = 0
            for j in range(-1,2):
                for k in range(-1,2):
                    d = (x+k,y+j)
                    i = i*2
                    if d in g:
                        i += 1
                    elif ogon and (d[0] < minx or d[0] > maxx or d[1] < miny or d[1] > maxy):
                        i += 1
            if m[i] == 1:
                ng.add((x,y))

    if zeroflip:
        ogon = not ogon

    minx = min([x for (x,y) in ng])
    miny = min([y for (x,y) in ng])
    maxx = max([x for (x,y) in ng])
    maxy = max([y for (x,y) in ng])

    for y in range(miny-1,maxy+2):
        s = ''
        for x in range(minx-1,maxx+2):
            if (x,y) in ng:
                s += '#'
            else:
                s += '.'
        #print(s)
    g = ng
print(len(ng))
