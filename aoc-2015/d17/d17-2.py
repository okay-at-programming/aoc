cons = (20, 15, 10, 5, 5)
cons = tuple([int(i) for i in open('data')])

def ways(c, l, a):
    if l == 0:
        return {a: 1}
    elif l < 0 or not c:
        return {}

    m = {}
    for i in range(len(c)):
        w = ways(c[i+1:], l-c[i], a+1)
        for k,v in w.items():
            m[k] = m.get(k, 0) + v
    return m

print(ways(cons, 150, 0))

