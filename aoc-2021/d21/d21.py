p=[4,8]
p=[1,6]
ps = [0,0]
d = 0
ap = 0
rc = 0

while ps[0] < 1000 and ps[1] < 1000:
    m = 0
    for _ in range(3):
        d += 1
        rc += 1
        if d > 100:
            d -= 100
        m += d
    p[ap] += m
    while p[ap] > 10:
        p[ap] -= 10
    ps[ap] += p[ap]

    ap = (ap+1)%2


print(rc,p,ps)
print(rc*ps[ap])


