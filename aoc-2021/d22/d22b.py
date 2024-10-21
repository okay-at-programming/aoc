grid = []

for l in open('test'):
    l = l.strip()
    on = l.split()[0] == 'on'
    c = []
    for x in l.split()[1].split(','):
        c.extend([int(x) for x in x.split('=')[1].split('..')])

    grid.append((c[0],c[1],c[2],c[3],c[4],c[5],on))

s = 0
on = []
off = []

def ol(c,o):
    xmi = max(c[0],o[0])
    xma = min(c[1],o[1])
    ymi = max(c[2],o[2])
    yma = max(c[3],o[3])
    zmi = min(c[4],o[4])
    zma = min(c[5],o[5])

    if xmi <= xma and ymi <= yma and zmi <= zma:
        return (xma-xmi+1) * (yma-ymi+1) * (zma-zmi+1)
    return 0

def area(c):
    return (c[1]-c[0]+1) * (c[3]-c[2]+1) * (c[5]-c[4]+1)


for c in grid:
    if c[6]:
        s += area(c)

        for o in on:
            s -= ol(c,o)
        for o in off:
            s += ol(c,o)

        on.append(c)
    else:

        for o in on:
            s -= ol(c,o)

        off.append(c)
    print(s)
print(s)

