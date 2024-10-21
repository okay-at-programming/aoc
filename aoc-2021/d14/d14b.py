m = {}

for l in open('test'):
    if '-' in l:
        a,b = l.strip().split(' -> ')
        m[a] = b
    elif l.strip():
        p = list(l.strip())

for j in range(10):
    np = []

    i = 1
    while i < len(p):
        ss = ''.join(p[i-1:i+2])
        if i > 1 and ss in m:
            np.extend(list(m[ss]))
            i += 2
            continue
        np.append(p[i-1])
        np.append(m[''.join(p[i-1:i+1])])
        if i > 1:
            m[ss] = ''.join(np[-6:])
            print(ss,m[ss])
        i += 1
    if i-1 < len(p):
        np.append(p[-1])
    p = np

    print(j,len(p))

c = {}
for i in p:
    c[i] = c.get(i,0) + 1

ma = max([j for i,j in c.items()])
mi = min([j for i,j in c.items()])

print(ma-mi)
