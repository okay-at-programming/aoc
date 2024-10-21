import sys

pc = 0

if len(sys.argv) > 1:
    pc = int(sys.argv[1])

m,pas = open('data').read().split('\n\n')

off = {}

def getdir(d):
    if d == 'n':
        return 3
    if d == 'e':
        return 0
    if d == 's':
        return 1
    if d == 'w':
        return 2

def getrange(x,y):
    if '-' in x:
        a = int(x.split('-')[0])
        b = int(x.split('-')[1])
        o = int(y)
        if a < b:
            return [(i,o) for i in range(a,b+1)]
        return [(i,o) for i in range(a,b-1,-1)]
    a = int(y.split('-')[0])
    b = int(y.split('-')[1])
    o = int(x)
    if a < b:
        return [(o,i) for i in range(a,b+1)]
    return [(o,i) for i in range(a,b-1,-1)]



for l in open('square'):
    s,e = l.strip().split(' -> ')

    sx,sy,sd = [c.strip() for c in s.split(',')]
    ex,ey,ed = [c.strip() for c in e.split(',')]

    sr = getrange(sx,sy)
    sd = getdir(sd)
    er = getrange(ex,ey)
    ed = getdir(ed)

    for i in range(50):
        off[(sr[i],sd)] = er[i],ed

g = {}
y = 1
for l in m.split('\n'):
    x = 1
    for c in l:
        if c in ('#','.'):
            g[(x,y)] = c
        x += 1
    y += 1

p = min(x for x,y in g.keys() if y == 1),1
d = 0
print(p)

dirs = ((1,0),(0,1),(-1,0),(0,-1))

path = {}
path[p] = 'a'
pi = 1
pci = 0

i = 0
while i < len(pas):
    if pci == pc:
        si = i
    j = i
    while pas[j].isnumeric():
        j += 1
    steps = int(pas[i:j])
    i = j

    for _ in range(steps):
        np = p[0]+dirs[d][0],p[1]+dirs[d][1]
        nd = None

        if np not in g:
            np,nd = off[(p,d)]

        if g[np] == '#':
            break

        p = np
        if nd != None:
            if pci == pc:
                print('nd')
            d = nd
        if pci == pc:
            path[p] = chr(ord('a') + pi)
            pi = (pi+1)%26

    if pci == pc:
        print(pas[si:i+1])
    if pas[i] == 'R':
        d = (d+1)%4
    elif pas[i] == 'L':
        d = (d-1)%4
    i += 1
    pci += 1

print(1000*p[1]+4*p[0]+d)
maxx = max(x for x,y in g)
maxy = max(y for x,y in g)


for y in range(maxy):
    s = ''
    for x in range(maxy):
        if (x,y) in path:
            s += path[(x,y)]
        elif (x,y) in g:
            s += g[(x,y)]
        else:
            s += ' '
    print(s)

