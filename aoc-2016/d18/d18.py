
row = '.^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^'
rowc = 39

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
        floor.add((x,0))

for y in range(1, rowc+1):

    for x in range(len(row)):
        if traps([(x-1,y-1),(x,y-1)],[(x+1,y-1)],floor):
            floor.add((x,y))
        if traps([(x+1,y-1),(x,y-1)],[(x-1,y-1)],floor):
            floor.add((x,y))
        if traps([(x-1,y-1)],[(x,y-1),(x+1,y-1)],floor):
            floor.add((x,y))
        if traps([(x+1,y-1)],[(x,y-1),(x-1,y-1)],floor):
            floor.add((x,y))


for r in range(rowc+1):
    s = ''
    for c in range(len(row)):
        s += '^' if (c,r) in floor else '.'
    print(s)

print(len(row)*(1+rowc) - len(floor))
