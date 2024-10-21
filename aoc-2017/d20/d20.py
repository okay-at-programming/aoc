def parse(line, i):
    l = line.split('>')[i]
    j = l.index('<')
    k = l[j+1:].split(',')
    return [int(n) for n in k]

points = []

for i,line in enumerate(open('data')):
    p = parse(line, 0)
    v = parse(line, 1)
    a = parse(line, 2)
    points.append([p,v,a,i])

closest = {}

for _ in range(100000):

    m = None
    mn = None

    for p in points:

        for i in range(3):
            p[1][i] += p[2][i]

        for i in range(3):
            p[0][i] += p[1][i]

        d = sum([abs(n) for n in p[0]])

        if not m or d < m:
            m = d
            mn = p[3]

    closest[mn] = closest.get(mn,0) + 1

    if max(closest.values()) > 1000:
        print(mn)
        break


print(closest)
