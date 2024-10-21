from z3 import Optimize, Int, Or

x = Int('x')
o = Optimize()
o.add(x >= 0)
o.add(x <= 4294967295)

for l in open('data'):
    a,b = l.strip().split('-')
    a,b = int(a),int(b)
    o.add(Or(x < a, x > b))

m = o.minimize(x)
print(o)
print(o.check())
print(m.value())
