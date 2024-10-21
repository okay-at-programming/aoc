coords = set()

for line in open('data', 'r'):
    coord = line.split(', ')
    coord = int(coord[0]), int(coord[1])
    coords.add(coord)

imax = 0
jmax = 0

for coord in coords:

    if coord[0] > imax:
        imax = coord[0]

    if coord[1] > jmax:
        jmax = coord[1]

imax += 2
jmax += 2

counts = {}
for c in coords:
    counts[c] = 0

maxdist = 10000
size = 0

for i in range(imax):
    for j in range(jmax):

        total = 0

        for c in coords:
            dist = abs(c[0] - i) + abs(c[1] - j)
            total += dist

        if total < maxdist:
            size += 1

print(size)


