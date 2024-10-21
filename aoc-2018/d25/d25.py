import sys

fn = sys.argv[1] if len(sys.argv) > 1 else 'data'

cs = []
ps = []

for l in open(fn):
    p = tuple(int(x) for x in l.strip().split(','))
    ps.append(p)

for p in ps:
    fc = []
    for c in cs:
        for s in c:
            md = sum([abs(x - y) for x,y in zip(p, s)])
            if md <= 3:
                fc.append(c)
                break
    if len(fc) == 1:
        fc[0].append(p)
    elif fc:
        nc = [p]
        for c in fc:
            nc.extend(c)
            cs.remove(c)
        cs.append(nc)
    else:
        cs.append([p])

print(cs)
print(len(cs))
