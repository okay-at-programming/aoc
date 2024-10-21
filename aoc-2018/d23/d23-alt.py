from z3 import *

bots = []

for line in open('data'):
    s = line.index('<') + 1
    e = line.index('>')
    rind = line.index('r') + 2
    x,y,z = [int(i) for i in line[s:e].split(',')]
    r = int(line[rind:])

    bots.append((r,(x,y,z)))


def zabs(x):
    return If(x >= 0, x, -x)

x,y,z = Int('x'),Int('y'),Int('z')
inrange = [Int(f'inrange_{i}') for i in range(len(bots))]

o = Optimize()
for i in range(len(bots)):
    br,(bx,by,bz) = bots[i]
    o.add(inrange[i] == If(zabs(bx-x) + zabs(by-y) + zabs(bz-z) <= br, 1, 0))

total = Int('total')
o.add(total == sum(inrange))

dist = Int('dist')
o.add(dist == zabs(x) + zabs(y) + zabs(z))

h1 = o.maximize(total)
h2 = o.minimize(dist)
print(o.check())
model = o.model()
print('x = ', model[x], 'y =', model[y],'z =', model[z], 'p =',model[dist])
