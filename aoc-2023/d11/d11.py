from collections import deque

gs = set()

data = [l.strip() for l in open('data')]

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
            ya = sum([1 for v in range(y) if v not in brws])
            xa = sum([1 for v in range(x) if v not in bcs])

            gs.add((x+xa,y+ya))

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
                dists += dist
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

print(total)
