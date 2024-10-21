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
                p = x,y
        x += 1
    y += 1

q = deque()
q.append((p,set(),0))

seen = set()

while q:
    p,d,s = q.popleft()

    if p in digs:
        d.add(p)
    if d == digs:
        print(s)
        break

    fd = frozenset(d)
    if (p,fd) in seen:
        continue
    seen.add((p,fd))

    for dr in ((0,1),(1,0),(0,-1),(-1,0)):
        pd = p[0]+dr[0],p[1]+dr[1]
        if pd in grid:
            continue
        dd = set(d)
        q.append((pd,dd,s+1))
