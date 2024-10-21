from collections import deque

m = set()
x,y = 0,0
m.add((0,0))

dirs = {'R':(1,0),'D':(0,1),'L':(-1,0),'U':(0,-1)}

for l in open('data'):
    d,s,_ = l.split()
    s = int(s)

    for i in range(s):
        x,y = x+dirs[d][0],y+dirs[d][1]
        m.add((x,y))

minx = min(x for x,y in m)
miny = min(y for x,y in m)
maxx = max(x for x,y in m)
maxy = max(y for x,y in m)


def f(x,y):
    if (x,y) in m:
        return True,m

    q = deque()
    q.append((x,y))
    seen = set()

    while q:
        x,y = q.popleft()

        if not (minx<=x<=maxx and miny<=y<=maxy):
            return False, seen

        if (x,y) in m:
            continue

        if (x,y) in seen:
            continue

        seen.add((x,y))

        for dx,dy in dirs.values():
            nx,ny = x+dx,y+dy
            q.append((nx,ny))

    return True, seen

a = set()
b = set()
for y in range(miny,maxy+1):
    for x in range(minx,maxx+1):
        if (x,y) in a:
            continue
        if (x,y) in b:
            continue
        v,s = f(x,y)
        if v:
            a |= s
        else:
            b |= s

print(len(a))
