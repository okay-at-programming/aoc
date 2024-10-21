progs = {}

for line in open('data'):
    key = int(line.split()[0])
    vals = [int(x) for x in ''.join(line.split()[2:]).split(',')]
    progs[key] = vals

groups = set()
groups.add(0)
c = 0
for s in progs.keys():
    seen = set()
    q = [s]
    while len(q) > 0:
        p = q.pop(0)

        if p in groups:
            break

        if p in seen:
            continue
        seen.add(p)

        for r in progs[p]:
            q.append(r)

    groups.add(p)

print(len(groups))
