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
t4 = r + 3*(w+1)
ts = {t1,t2,t3,t4}
maxs = max(ts)
q = deque([(p,0)])
es = {}
seen = (set(),set())
while q:
    p,s = q.popleft()

    lx = p[0]%(w+1)
    ly = p[1]%(h+1)
    if (lx,ly) in g:
        continue

    if s > maxs:
        continue

    if p in seen[s%2]:
        continue

    if s in ts:
        es[s] = es.get(s,len(seen[s%2])) + 1

    seen[s%2].add(p)

    x,y = p
    for dx,dy in ((x+1,y),(x,y+1),(x-1,y),(x,y-1)):
        q.append(((dx,dy),s+1))

print(len(es))
for k,v in es.items():
    print(k,v)

n1 = es[t1]
n2 = es[t2]
n3 = es[t3]

d1 = n2-n1
d2 = n3-n2

dd = d2-d1

a = dd//2
b = d1-3*a
c = n1-b-a

n = 3
ans = n1 + d1*n + ((n*(n-1))//2)*dd
assert ans == es[t4]

n = t//131
ans = n1 + d1*n + ((n*(n-1))//2)*dd
print(ans)


