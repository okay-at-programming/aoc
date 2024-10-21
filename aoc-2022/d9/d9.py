t = 0,0
h = 0,0

dirs = {'U':(0,1),'R':(1,0),'D':(0,-1),'L':(-1,0)}

hs = set()
hs.add(h)

for l in open('data'):
    d,s = l.strip().split()
    d = dirs[d]
    s = int(s)

    for _ in range(s):
        t = t[0]+d[0],t[1]+d[1]
        t0,t1 = t
        h0,h1 = h

        if abs(t0-h0) <= 1 and abs(t1-h1) <= 1:
            continue

        t0,t1 = t
        h0,h1 = h

        if t0 != h0 and t1 != h1:
            if t0 < h0:
                h0 -= 1
            else:
                h0 += 1
            if t1 < h1:
                h1 -= 1
            else:
                h1 += 1
        else:
            if t0 < h0:
                h0 -= 1
            elif t0 > h0:
                h0 += 1
            elif t1 < h1:
                h1 -= 1
            elif t1 > h1:
                h1 += 1
        h = h0,h1

        hs.add(h)

        #print()
        for y in range(6):
            s = ''
            for x in range(6):
                if (x,y) == h:
                    s += 'H'
                elif (x,y) == t:
                    s += 'T'
                else:
                    s += '.'
            #print(s)


print(len(hs))
