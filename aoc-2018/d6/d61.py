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

for i in range(imax):
    for j in range(jmax):

        sd = None
        sdc = None

        for c in coords:
            dist = abs(c[0] - i) + abs(c[1] - j)
            if sd is not None and sd == dist:
                sdc = None
            if sd is None or dist < sd:
                sd = dist
                sdc = c

        if sdc != None and (i == 0 or j == 0 or i+1 == imax or j+1 == jmax):
            counts[sdc] = None

        if sdc != None and counts[sdc] != None:
            counts[sdc] += 1

mc = None
for i, j in counts.items():
    if mc == None or j > counts[mc]:
        mc = i

print(mc, counts[mc])


