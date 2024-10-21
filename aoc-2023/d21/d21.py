from collections import deque

g = set()
w = 0
h = 0
for y,l in enumerate(open('data')):
    for x,c in enumerate(l.strip()):
        if c == '#':
            g.add((x,y))
        elif c == 'S':
            p = x,y
        w = max(w,x)
        h = max(h,y)


ms = 0
q = deque([(p,0)])
es = set()
seen = set()
while q:
    p,s = q.popleft()

    if p in g:
        continue

    if s > ms:
        print(s)
        ms = s

    if s == 64:
        es.add(p)
        continue

    if (p,s) in seen:
        continue

    seen.add((p,s))

    x,y = p
    for dx,dy in ((x+1,y),(x,y+1),(x-1,y),(x,y-1)):
        if 0<=dx<=w and 0<=dy<=h:
            q.append(((dx,dy),s+1))

print(len(es))

