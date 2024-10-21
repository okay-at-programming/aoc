
row = '.^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^'
rowc = 400000 - 1

floor = set()

def traps(i,o,floor):
    for x in i:
        if x not in floor:
            return False
    for x in o:
        if x in floor:
            return False
    return True

for x in range(len(row)):
    if row[x] == '^':
        floor.add(x)

count = len(floor)

for _ in range(1, rowc+1):
    nf = set()

    for x in range(len(row)):
        if traps([x-1,x],[x+1],floor):
            nf.add(x)
        if traps([x+1,x],[x-1],floor):
            nf.add(x)
        if traps([x-1],[x,x+1],floor):
            nf.add(x)
        if traps([x+1],[x,x-1],floor):
            nf.add(x)

    count += len(nf)
    floor = nf

print((rowc+1)*len(row) - count)
