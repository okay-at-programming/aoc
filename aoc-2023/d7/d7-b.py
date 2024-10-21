def p(c):
    m = {'A': 14, 'K': 13,'Q':12,'J':1, 'T': 10}
    if c in m:
        return m[c]
    return int(c)

def valj(oh):

    b = 0
    for h in rpjs(oh):
        m = {}
        for c in h:
            m[c] = m.get(c, 0) + 1

        fv = None
        s = sorted(list(m.values()), reverse=True)
        if s == [5]:
            fv= 7
        elif s == [4, 1]:
            fv= 6
        elif s == [3, 2]:
            fv= 5
        elif s == [3,1,1]:
            fv= 4
        elif s == [2,2,1]:
            fv= 3
        elif s == [2,1,1,1]:
            fv= 2
        elif s == [1,1,1,1,1]:
            fv= 1
        else:
            assert False

        b = max(fv, b)


    return b, p(oh[0]), p(oh[1]), p(oh[2]), p(oh[3]), p(oh[4])

def rp(c, os):
    if c != 'J':
        return [c]

    return os

def rpjs(h):
    if 'J' not in h:
        return [h]
    os = []
    for c in h:
        if c != 'J' and c not in os:
            os.append(c)

    if not os:
        os = ['J']

    r = []
    for a in rp(h[0], os):
        for b in rp(h[1], os):
            for c in rp(h[2], os):
                for d in rp(h[3], os):
                    for e in rp(h[4], os):
                        r.append(a+b+c+d+e)
    return r

ls = []
for l in open('data'):
    cards, bid = l.split()
    bid = int(bid)

    ls.append((cards, bid, valj(cards)))


ls = sorted(ls, key=lambda x: x[2])

v = 0
for i,l in enumerate(ls):
    v += (i+1)*l[1]

print(v)
