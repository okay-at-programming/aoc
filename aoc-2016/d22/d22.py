nodes = set()

for l in open('data'):
    if not l.startswith('/dev/'):
        continue
    l = l.split()

    x = int(l[0].split('-')[1][1:])
    y = int(l[0].split('-')[2][1:])
    used = int(l[2][:-1])
    avail = int(l[3][:-1])
    nodes.add((x,y,used,avail))

t = 0
for a in nodes:
    if a[2] == 0:
        continue
    for b in nodes:
        if a == b:
            continue

        if a[2] <= b[3]:
            t += 1

print(t)

