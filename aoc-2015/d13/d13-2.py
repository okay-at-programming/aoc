guests = set()
hapmap = {}

for l in open('data'):
    a = l.split()[0]
    p = int(l.split()[3])
    if l.split()[2] == 'lose':
        p *= -1
    b = l.split()[-1][:-1]

    hapmap[(a,b)] = p
    guests.add(a)

rob = 'rob'

for g in guests:
    hapmap[(g,rob)] = 0
    hapmap[(rob,g)] = 0

guests.add(rob)

def perm(l, r):
    if len(r) == 0:
        return [l]
    ret = []
    for a in r:
        nr = set(r)
        nr.remove(a)
        nl = list(l)
        nl.append(a)
        ret.extend(perm(nl, nr))
    return ret

happs = []
for p in perm([], guests):
    t = 0
    for i in range(len(p)):
        a = p[i]
        b = p[i+1] if i+1 < len(p) else p[0]
        t += hapmap[(a,b)]
        t += hapmap[(b,a)]
    happs.append(t)
print(max(happs))


