m = {}

for l in open('data'):
    if '-' in l:
        a,b = l.strip().split(' -> ')
        m[a] = (a[0]+b,b+a[1])
    elif l.strip():
        p = l.strip()

cs = {}
i = 1
while i < len(p):
    ss = p[i-1:i+1]
    cs[ss] = cs.get(ss,0) + 1
    i += 1

lc = p[-1]


for j in range(40):
    ncs = {}
    for k,v in cs.items():
        a,b = m[k]
        ncs[a] = ncs.get(a,0) + v
        ncs[b] = ncs.get(b,0) + v
    cs = ncs

c = {}
for a,b in cs.items():
    i = a[0]
    c[i] = c.get(i,0) + b
c[lc] += 1

ma = max([j for j in c.values()])
mi = min([j for j in c.values()])

print(ma-mi)
