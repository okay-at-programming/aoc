comps = []

for l in open('data'):
    a,b = [int(x) for x in l.strip().split('/')]

    comps.append((a,b))



def path(total, c, d, l):

    m = total
    ml = d

    for i,(a,b) in enumerate(l):
        if a == c:
            r,rd = path(total + a + b, b, d+1, l[:i] + l[i+1:])
            if rd >= ml and r > m:
                m = r
                ml = rd
        if b == c:
            s,sd = path(total + a + b, a, d+1, l[:i] + l[i+1:])
            if sd >= ml and s > m:
                m = s
                ml = sd

    return m,ml


m,d = path(0,0,0,comps)
print(m,d)
