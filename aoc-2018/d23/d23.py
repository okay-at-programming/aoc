best = None

bots = []

for line in open('data'):
    s = line.index('<') + 1
    e = line.index('>')
    rind = line.index('r') + 2
    x,y,z = [int(i) for i in line[s:e].split(',')]
    r = int(line[rind:])

    bots.append((r,(x,y,z)))

    if not best or r > best[0]:
        best = (r,(x,y,z))

c = 0

for bot in bots:
    d = 0

    for i in range(3):
        d += abs(bot[1][i]-best[1][i])

    if d <= best[0]:
        c += 1

print(c)
