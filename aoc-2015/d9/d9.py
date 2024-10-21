dists = {}
locs = set()

for l in open('data'):
    a = l.split()[0]
    b = l.split()[2]
    d = int(l.split()[-1])
    locs.add(a)
    locs.add(b)

    dists[(a,b)] = d
    dists[(b,a)] = d


def perm(l, d, e):
    if len(l) == 0:
        return d
    s = []
    for c in l:
        nl = set(l)
        nl.remove(c)
        nd = d + dists[(c,e)]
        s.append(perm(nl,nd,c))
    return max(s)

def start_perm(l):
    s = []
    for c in l:
        nl = set(l)
        nl.remove(c)
        s.append(perm(nl,0,c))
    return max(s)

print(start_perm(locs))
