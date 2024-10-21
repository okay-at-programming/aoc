from collections import deque

t = 26501365
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

r = t%(w+1)
t1 = r
t2 = r+w+1
t3 = r + 2*(w+1)
ts = {t1,t2,t3}
maxs = max(ts)
ms = 0
q = deque([(p,0)])
es = {}
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

    if s > maxs:
        continue

    if (p,s) in seen:
        continue

    seen.add((p,s))

    if s in ts:
        if s not in es:
            es[s] = set()
        es[s].add(p)

    x,y = p
    for dx,dy in ((x+1,y),(x,y+1),(x-1,y),(x,y-1)):
        q.append(((dx,dy),s+1))

print(len(es))
for k,v in es.items():
    print(k,len(v))

n1 = len(es[t1])
n2 = len(es[t2])
n3 = len(es[t3])

d1 = n2-n1
d2 = n3-n2

dd = d2-d1

a = dd//2
b = d1-3*a
c = n1-b-a

n = t//131
ans = n1 + d1*n + ((n*(n-1))//2)*dd
print(ans)


