from collections import deque

g = [l.strip() for l in open('data')]

seen = {}

dirs = {'E': (1,0), 'S': (0,1), 'W': (-1,0), 'N': (0,-1)}

q = deque()
q.append((0,0,'E'))

ex = {}


while q:
    x,y,d = q.popleft()

    seen[(x,y)] = seen.get((x,y), 0) + 1

    ec = ex.get((x,y,d),0)
    if ec > 2:
        continue

    ex[(x,y,d)] = ec + 1

    c = g[y][x]

    nds = []

    if d == 'E' and c in '|\/':
        if c in '\|':
            nds.append('S')
        if c in '/|':
            nds.append('N')
    elif d == 'S' and c in '-\/':
        if c in '\-':
            nds.append('E')
        if c in '/-':
            nds.append('W')
    elif d == 'W' and c in '|\/':
        if c in '\|':
            nds.append('N')
        if c in '/|':
            nds.append('S')
    elif d == 'N' and c in '-\/':
        if c in '\-':
            nds.append('W')
        if c in '/-':
            nds.append('E')
    else:
        nds.append(d)

    for nd in nds:
        nx,ny = x+dirs[nd][0],y+dirs[nd][1]
        if 0<=nx<len(g[0]) and 0<=ny<len(g):
            q.append((nx,ny,nd))

t = 0
for y in range(len(g)):
    s = ''
    for x in range(len(g[0])):
        if (x,y) in seen:
            s += '#'
            if seen[(x,y)] >= 1:
                t += 1
        else:
            s += '.'
    print(s)

print(t)
