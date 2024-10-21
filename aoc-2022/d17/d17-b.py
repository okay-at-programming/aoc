
shapes = (
        ((0,0),(1,0),(2,0),(3,0)),
        ((1,0),(0,1),(1,1),(2,1),(1,2)),
        ((0,0),(1,0),(2,0),(2,1),(2,2)),
        ((0,0),(0,1),(0,2),(0,3)),
        ((0,0),(1,0),(0,1),(1,1)))


w = open('test').read().strip()

si = 0
wi = 0

h = -1
g = set([(0,-1),(1,-1),(2,-1),(3,-1),(4,-1),(5,-1),(6,-1)])

seen = {}

def tops(g):
    t = [max(y for x,y in g if x == i) for i in range(7)]
    m = min(t)
    return tuple(y-m for y in t)


for j in range(1000000000000):
    if j%100000000 == 0:
        print(j)
    cs = [(x+2,y+h+4) for x,y in shapes[si]]

    top = tops(g)
    key = (wi,si,top)
    if key in seen:
        print('rep',j)
        nh, nt, nwi = seen[key]
        h += nh
        m = max(nt)
        g.update([(i,h-m+nt[i]) for i in range(7)])
        wi = (wi+nwi)%len(w)
        continue

    si = (si+1)%len(shapes)
    nwi = 0

    while True:
        nwi += 1
        cw = w[wi]
        if cw == '<':
            cw = -1
        else:
            cw = 1
        wi = (wi+1)%len(w)

        ncs = []
        for x,y in cs:
            if 0<=x+cw<7 and (x+cw,y) not in g:
                ncs.append((x+cw,y))
            else:
                ncs = cs
                break

        stop = False

        nncs = []
        for x,y in ncs:
            if (x,y-1) not in g:
                nncs.append((x,y-1))
            else:
                nncs = ncs
                stop = True
                break

        cs = nncs

        if stop:
            break

    sm = max(y for x,y in cs)
    nh = sm - h
    h = max(sm,h)
    g.update(cs)

    nt = tops(g)

    seen[key] = (nh, nt, nwi)




print(h+1)


def printout():
    print()
    print(h)
    print(ws)
    for y in range(h+1,-1,-1):
        s = '|'
        for x in range(7):
            if (x,y) in g:
                s += '#'
            else:
                s += ' '
        print(s+'|')











