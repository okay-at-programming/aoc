from z3 import *

hs = []

ll = 200000000000000
ul = 400000000000000

for l in open('data'):
    ps,vs = l.strip().split(' @ ')
    ps = [int(x) for x in ps.split(', ')]
    vs = [int(x) for x in vs.split(', ')]

    hs.append((ps,vs))

c = 0
for i,(aps,avs) in enumerate(hs):
    for j,(bps,bvs) in enumerate(hs):
        if i >= j:
            continue

        #print(aps,avs,bps,bvs)

        x = Real('x')
        y = Real('y')
        axt = Real('axt')
        ayt = Real('ayt')
        bxt = Real('bxt')
        byt = Real('byt')
        s = Solver()
        s.add(ll<=x, x<=ul)
        s.add(ll<=y, y<=ul)

        s.add(x == aps[0] + avs[0]*axt)
        s.add(x == bps[0] + bvs[0]*bxt)
        s.add(y == aps[1] + avs[1]*ayt)
        s.add(y == bps[1] + bvs[1]*byt)

        s.add(axt >= 0)
        s.add(bxt >= 0)
        s.add(ayt >= 0)
        s.add(byt >= 0)

        s.add(y == aps[1] + (avs[1]/avs[0])*(x-aps[0]))
        s.add(y == bps[1] + (bvs[1]/bvs[0])*(x-bps[0]))

        #print(s.check())
        if s.check() == sat:
            #print(s.model())
            c += 1
        #print()
    print(i,len(hs))

print(c)
