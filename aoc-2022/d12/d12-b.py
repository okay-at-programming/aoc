from collections import deque

m = []

Ss = []
E = None
y = 0

for l in open('data'):
    l = l.strip()
    s = ''
    x = 0
    for c in l:
        if c in ('a','S'):
            Ss.append((x,y))
            s += 'a'
        elif c == 'E':
            E = x,y
            s += 'z'
        else:
            s += c
        x += 1
    m.append(s)
    y += 1

sp = None
ms = 100000
for S in Ss:
    s = set()
    q = deque()
    q.append((S,0,set()))

    while len(q) > 0:
        p, steps,path = q.popleft()

        if p == E:
            ms = min(ms,steps)
            if ms == steps:
                sp = path
                sp.add(p)
            break

        if steps > ms:
            break

        if p in s:
            continue

        s.add(p)
        path.add(p)

        x,y = p

        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx,ny = x+dx,y+dy
            if 0<=nx<len(m[0]) and 0<=ny<len(m):
                c = ord(m[ny][nx]) - ord(m[y][x])
                if c <= 1:
                    ns = set(path)
                    q.append(((nx,ny),steps+1, ns))

print(ms)
y = 0
for l in m:
    x = 0
    s = ''
    for c in l:
        if (x,y) in sp:
            s += 'X'
        else:
            s += c
        x += 1
    y += 1
    print(s)
