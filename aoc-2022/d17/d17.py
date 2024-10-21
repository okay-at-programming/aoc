
shapes = (
        ((0,0),(1,0),(2,0),(3,0)),
        ((1,0),(0,1),(1,1),(2,1),(1,2)),
        ((0,0),(1,0),(2,0),(2,1),(2,2)),
        ((0,0),(0,1),(0,2),(0,3)),
        ((0,0),(1,0),(0,1),(1,1)))


w = open('data').read().strip()

si = 0
wi = 0

h = -1
g = set([(0,-1),(1,-1),(2,-1),(3,-1),(4,-1),(5,-1),(6,-1)])

for _ in range(2022):
    cs = [(x+2,y+h+4) for x,y in shapes[si]]
    si = (si+1)%len(shapes)

    ws = ''
    while True:
        cw = w[wi]
        ws += cw
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











