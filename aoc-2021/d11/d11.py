o = {}

y = 0
xmax = 0
for l in open('data'):
    x = 0
    for c in l.strip():
        o[(x,y)] = int(c)
        x += 1
    xmax = x
    y += 1
ymax = y

f = 0

for _ in range(100):
    q = []
    for x in range(xmax):
        for y in range(ymax):
            q.append((x,y))

    i = 0
    while i < len(q):
        x,y = q[i]
        i += 1
        if (x,y) not in o:
            continue
        if o[(x,y)] == 0 and i-1 >= xmax*ymax:
            continue
        elif o[(x,y)] == 9:
            o[(x,y)] = 0
            f += 1
            for dx,dy in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
                q.append((x+dx,y+dy))
        else:
            o[(x,y)] += 1

    for y in range(ymax):
        s = ''
        for x in range(xmax):
            s += str(o[(x,y)])
        print(s)
    print()
print(f)
