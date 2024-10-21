
t = 0

for l in open('data'):
    gid = int(l.split()[1][:-1])
    print(gid)

    m = {'red': 0, 'green': 0, 'blue': 0}
    for p in l.split(': ')[1].split(';'):
        for h in p.split(','):
            c = int(h.strip().split()[0])
            colour = h.strip().split()[1]

            m[colour] = max(c, m[colour])

    ct = 1
    for v in m.values():
        ct *= v

    t += ct

print(t)



