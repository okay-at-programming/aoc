from random import shuffle

rules = []

for l in open('test2'):
    if not l:
        continue
    elif '=>' in l:
        a = tuple([c.strip() for c in l.split('=>')])

        rules.append(a)
    else:
        molecule = l.strip()

mol = molecule

mc = 0
c = 0
f = 1
while mol != 'e':
    m1 = mol
    for r in rules:
        s = mol.find(r[1])
        if s > 0:
            mol = mol.replace(r[1],r[0],1)
            c += 1
    shuffle(rules)
    if m1 == mol:
        shuffle(rules)
        mol = molecule
        c = 0
        mc += 1
        if mc > f:
            print(mc)
            f *= 2
print(c)


