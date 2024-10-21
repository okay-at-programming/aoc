
m = {'red': 12, 'green': 13, 'blue': 14}
t = 0

for l in open('data'):
    gid = int(l.split()[1][:-1])
    print(gid)

    v = True
    for p in l.split(': ')[1].split(';'):
        for h in p.split(','):
            c = int(h.strip().split()[0])
            colour = h.strip().split()[1]

            if m[colour] < c:
                v = False

    if v:
        t += gid

print(t)



