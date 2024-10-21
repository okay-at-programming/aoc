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


for _ in range(10000):

    cols = {}

    for p in points:

        if p[3] == -1:
            continue

        for i in range(3):
            p[1][i] += p[2][i]

        for i in range(3):
            p[0][i] += p[1][i]

        spot = tuple(p[0])

        l = cols.get(spot,[])
        l.append(p[3])
        cols[spot] = l


    for l in cols.values():
        if len(l) > 1:
            for p in l:
                points[p][3] = -1

print(len([n for n in points if n[3] > 0]))

