from collections import deque

grid = set()
digs = set()
y = 0
for l in open('data'):
    x = 0
    for c in l.strip():
        if c == '#':
            grid.add((x,y))
        elif c.isdigit():
            digs.add((x,y))
            if c == '0':
                z = x,y
        x += 1
    y += 1

q = deque()
q.append((z,set(),False,0))

seen = set()

while q:
    p,d,h,s = q.popleft()

    if h and p == z:
        print(s)
        break
    if p in digs:
        d.add(p)
    if d == digs:
        print(s)
        d = set()
        h = True

    fd = frozenset(d)
    if (p,fd,h) in seen:
        continue
    seen.add((p,fd,h))

    for dr in ((0,1),(1,0),(0,-1),(-1,0)):
        pd = p[0]+dr[0],p[1]+dr[1]
        if pd in grid:
            continue
        dd = set(d)
        q.append((pd,dd,h,s+1))
