from z3 import *

mc = 4000000
mp = 4000000
points = []

for l in open('data'):
    s,b = l.split(':')
    sx = int(s.split('=')[1].split(',')[0])
    sy = int(s.split('=')[2])
    bx = int(b.split('=')[1].split(',')[0])
    by = int(b.split('=')[2])

    md = abs(bx-sx) + abs(by-sy)

    points.append((sx,sy,md))

def zabs(x):
    return If(x >= 0, x, -x)

x,y = Int('x'),Int('y')
s = Solver()
s.add(And(0 <= x, x <= mp))
s.add(And(0 <= y, y <= mp))

for p in points:
    mx,my,md = p
    s.add(zabs(mx-x) + zabs(my-y) > md)

print(s.check())
model = s.model()
print(model)

print(mc*model[x].as_long() + model[y].as_long())
