paths = {}

for l in open('data'):
    a,b = l.strip().split('-')
    c = paths.get(a,[])
    c.append(b)
    paths[a] = c
    c = paths.get(b,[])
    c.append(a)
    paths[b] = c

t = 0
q = [('start',set(),False)]

while len(q) > 0:
    p,v,twice = q.pop()

    if p == 'end':
        t += 1
        continue

    if len(v) > 0 and p == 'start':
        continue

    if p.islower() and p in v:
        if twice:
            continue
        twice = True

    v.add(p)

    for n in paths[p]:
        q.append((n,v.copy(),twice))

print(t)

