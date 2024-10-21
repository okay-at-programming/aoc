from collections import deque

m = []

q = deque()
E = None
y = 0

for l in open('data'):
    l = l.strip()
    s = ''
    x = 0
    for c in l:
        if c in ('a','S'):
            s += 'a'
            q.append(((x,y),0))
        elif c == 'E':
            E = x,y
            s += 'z'
        else:
            s += c
        x += 1
    m.append(s)
    y += 1

for l in m:
    print(l)


s = set()

while len(q) > 0:
    p, steps = q.popleft()

    if p == E:
        print(steps)
        break

    if p in s:
        continue

    s.add(p)

    x,y = p

    for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx,ny = x+dx,y+dy
        if 0<=nx<len(m[0]) and 0<=ny<len(m):
            c = ord(m[ny][nx]) - ord(m[y][x])
            if c <= 1:
                q.append(((nx,ny),steps+1))
