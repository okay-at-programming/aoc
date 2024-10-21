xs = set()
ys = set()
zs = set()

ins = []

for l in open('data'):
    l = l.strip()
    on = l.split()[0] == 'on'
    c = []
    for x in l.split()[1].split(','):
        c.extend([int(x) for x in x.split('=')[1].split('..')])

    for i in range(1,len(c),2):
        c[i] += 1

    c.append(on)

    xs.update(c[:2])
    ys.update(c[2:4])
    zs.update(c[4:6])

    ins.append(tuple(c))


xs = list(xs)
ys = list(ys)
zs = list(zs)
xs.sort()
ys.sort()
zs.sort()

print(len(xs))
print(len(ys))
print(len(zs))

zones = set()

i = 0

for l in ins:
    xmi = xs.index(l[0])
    xma = xs.index(l[1])
    ymi = ys.index(l[2])
    yma = ys.index(l[3])
    zmi = zs.index(l[4])
    zma = zs.index(l[5])

    for x in range(xmi,xma):
        for y in range(ymi,yma):
            for z in range(zmi,zma):
                if l[6]:
                    zones.add((xs[x],xs[x+1],ys[y],ys[y+1],zs[z],zs[z+1]))
                else:
                    zones.discard((xs[x],xs[x+1],ys[y],ys[y+1],zs[z],zs[z+1]))

    i += 1
    print(i,len(ins),len(zones))

i = 0
s = 0
for x1,x2,y1,y2,z1,z2 in zones:
    s += (x2-x1) * (y2-y1) * (z2-z1)
    i += 1
    if i%10000 == 0:
        print(len(zones)-i)
print(s)
