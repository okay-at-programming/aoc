def p(c):
    m = {'A': 14, 'K': 13,'Q':12,'J':11, 'T': 10}
    if c in m:
        return m[c]
    return int(c)

def val(h):
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

    return fv, p(h[0]), p(h[1]), p(h[2]), p(h[3]), p(h[4])

ls = []
for l in open('data'):
    cards, bid = l.split()
    bid = int(bid)

    ls.append((cards, bid, val(cards)))


ls = sorted(ls, key=lambda x: x[2])
print(ls)

v = 0
for i,l in enumerate(ls):
    v += (i+1)*l[1]

print(v)
