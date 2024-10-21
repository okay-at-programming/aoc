from collections import deque

g = [l.strip() for l in open('data')]


dirs = {'E': (1,0), 'S': (0,1), 'W': (-1,0), 'N': (0,-1)}

def f(p):
    q = deque()
    q.append(p)

    seen = set()
    ex = set()

    while q:
        x,y,d = q.popleft()

        if (x,y,d) in ex:
            continue

        seen.add((x,y))
        ex.add((x,y,d))

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

    return len(seen)

b = 0
for x in range(len(g[0])):
    bs = f((x,0,'S'))
    bn = f((x,len(g)-1,'N'))
    b = max(b,bs,bn)

for y in range(len(g)):
    be = f((0,y,'E'))
    bw = f((len(g[0])-1,y,'W'))
    b = max(b,be,bw)

print(b)

