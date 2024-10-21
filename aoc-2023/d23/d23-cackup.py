from queue import PriorityQueue
from collections import deque

g = {}

mx = 0
my = 0
for y,l in enumerate(open('data')):
    for x,c in enumerate(l.strip()):
        if c in '#':
            g[(x,y)] = c
        mx = max(x,mx)
        my = max(y,my)

mx += 1
my += 1

for x in range(mx):
    if (x,0) not in g:
        s = x,0
    if (x,my-1) not in g:
        e = x,my-1

edges = {}
for y in range(my):
    for x in range(mx):
        if (x,y) in g:
            continue
        for dx,dy in ((x+1,y),(x,y+1),(x-1,y),(x,y-1)):
            if (dx,dy) in g:
                continue
            if 0<=dx<mx and 0<=dy<my:
                if (x,y) not in edges:
                    edges[(x,y)] = set()
                edges[(x,y)].add((dx,dy,1))
                if (dx,dy) not in edges:
                    edges[(dx,dy)] = set()
                edges[(dx,dy)].add((x,y,1))

done = True
while done:
    done = False
    key = None
    for k,v in edges.items():
        if len(v) == 2:
            key = k
        if key:
            break

    if key and len(edges[key]) == 2:
        a,b = edges[key]
        edges[a[:2]].remove(k+(a[2],))
        edges[b[:2]].remove(k+(b[2],))
        edges[a[:2]].add((b[0],b[1],a[2]+b[2]))
        edges[b[:2]].add((a[0],a[1],a[2]+b[2]))
        edges.pop(key,None)
        done = True

print('searching')

q = []
q.append((s,0))
seen = set()
m = 0

while q:
    p,d = q.pop()

    if d == -1:
        seen.remove(p)
        continue

    if p == e:
        if d > m:
            print(d)
        m = max(m,d)
        continue

    if p in seen:
        continue
    seen.add(p)

    q.append((p,-1))

    for nx,ny,nd in edges[p]:
        q.append(((nx,ny),d+nd))

print('ans',m)

