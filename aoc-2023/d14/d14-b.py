m = {}

h = 0
w = 0
for y,l in enumerate(open('data')):
    h = max(h,y)
    for x,c in enumerate(l.strip()):
        w = max(w,x)
        if c in '#O':
            m[(x,y)] = c


def rotate(m,h,w):
    nm = {}
    for k,v in m.items():
        x,y = k
        ny = x
        nx = w - y
        nm[(nx,ny)] = v

    assert len(nm) == len(m)
    return nm

def tip(m, h, w):
    nm = {}
    for x in range(w+1):
        b = 0
        rc = 0
        for y in range(h+1):
            c = m.get((x,y),'.')
            if c == 'O':
                rc += 1
            elif c == '#':
                nm[(x,y)] = c
                for i in range(rc):
                    nm[(x,b+i)] = 'O'
                rc = 0
                b = y+1
        for i in range(rc):
            nm[(x,b+i)] = 'O'

    assert len(nm) == len(m)
    return nm

def score(m,h,w):
    s = 0
    for x in range(w+1):
        for y in range(h+1):
            if m.get((x,y),'.') == 'O':
                s += h+1-y
    return s


def printm(m, h, w):
    for y in range(h+1):
        s = ''
        for x in range(w+1):
            s += m.get((x,y),'.')
        print(s)
    print()

def cycle(m, h, w):
    for _ in range(4):
        m = tip(m,h,w)
        m = rotate(m,h,w)
        w,h = h,w
    s = score(m,h,w)
    return m,s

def key(m):
    l = []
    for k,v in m.items():
        if v == 'O':
            l.append(f'({k[0]},{k[1]})')

    return ''.join(sorted(l))

mm = m
m1 = m
m2 = m
m1,s1 = cycle(m1,h,w)
k1 = key(m1)
m2,s2 = cycle(m2,h,w)
m2,s2 = cycle(m2,h,w)
k2 = key(m2)

while k1 != k2:
    m1,s1 = cycle(m1,h,w)
    k1 = key(m1)
    m2,s2 = cycle(m2,h,w)
    m2,s2 = cycle(m2,h,w)
    k2 = key(m2)

mu = 0
m1 = mm
k1 = key(m1)
while k1 != k2:
    m1,s1 = cycle(m1,h,w)
    k1 = key(m1)
    m2,s2 = cycle(m2,h,w)
    k2 = key(m2)
    mu += 1

lam = 1
m2,s2 = cycle(m2,h,w)
k2 = key(m2)
while k1 != k2:
    m2,s2 = cycle(m2,h,w)
    k2 = key(m2)
    lam += 1

print(mu,lam)

l = 1000000000 - mu

i = mu + l%lam
print(i)
for _ in range(i):
    mm,s = cycle(mm,h,w)

print(s)

