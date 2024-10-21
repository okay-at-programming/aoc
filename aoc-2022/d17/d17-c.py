
shapes = (
        ((0,0),(1,0),(2,0),(3,0)),
        ((1,0),(0,1),(1,1),(2,1),(1,2)),
        ((0,0),(1,0),(2,0),(2,1),(2,2)),
        ((0,0),(0,1),(0,2),(0,3)),
        ((0,0),(1,0),(0,1),(1,1)))


w = open('data').read().strip()

si1 = 0
wi1 = 0

h1 = -1
floor = [(0,-1),(1,-1),(2,-1),(3,-1),(4,-1),(5,-1),(6,-1)]
g1 = set(floor)


def move(si, wi, g,h):
    cs = [(x+2,y+h+4) for x,y in shapes[si]]
    si = (si+1)%len(shapes)

    while True:
        cw = w[wi]
        if cw == '<':
            cw = -1
        elif cw == '>':
            cw = 1
        else:
            assert False
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
    h = max(sm,h)
    g.update(cs)

    return si,wi,g,h

def tops(g):
    t = [max(y for x,y in g if x == i) for i in range(7)]
    m = min(t)
    return tuple(y-m for y in t)

seen = {}

lim = 1000000000000
for j in range(lim):
    key = wi1,si1,tops(g1)
    if key in seen:
        pj,ph = seen[key]

        p = j - pj
        h = h1 - ph

        r = lim - j

        ri = r // p

        for k in range(r%p):
            si1,wi1,g1,h1 = move(si1,wi1,g1,h1)

        print(ri*h + h1 + 1)
        break

    seen[key] = j, h1
    si1,wi1,g1,h1 = move(si1,wi1,g1,h1)










