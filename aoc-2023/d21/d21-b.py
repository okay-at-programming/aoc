from collections import deque

t = 5000
g = set()
w = 0
h = 0
for y,l in enumerate(open('test')):
    for x,c in enumerate(l.strip()):
        if c == '#':
            g.add((x,y))
        elif c == 'S':
            p = x,y
        w = max(w,x)
        h = max(h,y)

print(w,h,t%w)

bs = {}
ms = 0
q = deque([(p,0)])
es = set()
seen = set()
while q:
    p,s = q.popleft()

    lx = p[0]%(w+1)
    ly = p[1]%(h+1)
    if (lx,ly) in g:
        continue

    if s > ms:
        print(s)
        ms = s



        es.add(p)
        bs[bd].add(p)
        break

    if (p,s) in seen:
        continue

    seen.add((p,s))

    x,y = p
    for dx,dy in ((x+1,y),(x,y+1),(x-1,y),(x,y-1)):
        q.append(((dx,dy),s+1))

print(len(es))
for k,v in bs.items():
    print(k, abs(k[0]) + abs(k[1]),len(v))
