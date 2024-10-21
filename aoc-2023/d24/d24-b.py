from z3 import *

hs = []


for l in open('data'):
    ps,vs = l.strip().split(' @ ')
    ps = [int(x) for x in ps.split(', ')]
    vs = [int(x) for x in vs.split(', ')]

    hs.append((ps,vs))


mx = Int('mx')
my = Int('my')
mz = Int('mz')
mvx = Int('mvx')
mvy = Int('mvy')
mvz = Int('mvz')
s = Solver()

for i,(ps,vs) in enumerate(hs):

    t = Int(f't-{i}')

    s.add(mx + mvx*t == ps[0] + vs[0]*t)
    s.add(my + mvy*t == ps[1] + vs[1]*t)
    s.add(mz + mvz*t == ps[2] + vs[2]*t)


print(s.check())
m = s.model()

print(m[mx],m[my],m[mz],' - ',m[mx].as_long()+m[my].as_long()+m[mz].as_long())

