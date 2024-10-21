comps = []

for l in open('data'):
    a,b = [int(x) for x in l.strip().split('/')]

    comps.append((a,b))



def path(total, c, l):

    m = total

    for i,(a,b) in enumerate(l):
        if a == c:
            r = path(total + a + b, b, l[:i] + l[i+1:])
            if r > m:
                m = r
        if b == c:
            s = path(total + a + b, a, l[:i] + l[i+1:])
            if s > m:
                m = s

    return m


m = path(0,0,comps)
print(m)
