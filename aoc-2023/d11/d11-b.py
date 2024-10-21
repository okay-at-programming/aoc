from collections import deque

gs = set()

data = [l.strip() for l in open('data')]
mult = 1000000 - 1

brws = set()
bcs = set()

for y,l in enumerate(data):
    for x,c in enumerate(l):
        if c == '#':
            brws.add(y)
            bcs.add(x)

print(brws)
print(bcs)

for y,l in enumerate(data):
    for x,c in enumerate(l):
        if c == '#':
            gs.add((x,y))

minx = min(x for x,_ in gs)
maxx = max(x for x,_ in gs)
miny = min(y for _,y in gs)
maxy = max(y for _,y in gs)

for y in range(maxy+1):
    s = ''
    for x in range(maxx+1):
        if (x,y) in gs:
            s += '#'
        else:
            s += '.'
    print(s)

def find(p):
    q = deque()
    q.append((p, 0))
    seen = set()

    dists = 0
    dc = 0

    while q:
        cp,dist = q.popleft()

        if cp in seen:
            continue
        seen.add(cp)

        if cp != p and cp in gs:
            if cp not in done:
                sx,ex = min(cp[0],p[0]),max(cp[0],p[0])
                sy,ey = min(cp[1],p[1]),max(cp[1],p[1])
                xadd = sum([mult for v in range(sx,ex) if v not in bcs])
                yadd = sum([mult for v in range(sy,ey) if v not in brws])
                dists += dist + xadd + yadd
                dc += 1

        x,y = cp

        for dx,dy in ((x+1,y),(x,y+1),(x-1,y),(x,y-1)):
            if 0<=dx<=maxx and 0<=dy<=maxy:
                q.append(((dx,dy),dist+1))

    return dists,dc

total = 0
dc = 0
done = set()
for p in gs:
    t,d= find(p)
    total += t
    dc += d
    done.add(p)

print(total,dc)
