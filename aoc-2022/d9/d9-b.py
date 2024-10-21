tt = 0,0
hl = [(0,0) for _ in range(9)]

dirs = {'U':(0,1),'R':(1,0),'D':(0,-1),'L':(-1,0)}

hs = set()
hs.add(hl[8])

for l in open('data'):
    d,s = l.strip().split()
    d = dirs[d]
    s = int(s)

    for _ in range(s):
        tt = tt[0]+d[0],tt[1]+d[1]
        for i in range(9):
            h = hl[i]
            if i == 0:
                t = tt
            else:
                t = hl[i-1]
            t0,t1 = t
            h0,h1 = h

            if abs(t0-h0) <= 1 and abs(t1-h1) <= 1:
                continue

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
            hl[i] = h

        hs.add(hl[8])

print(len(hs))
