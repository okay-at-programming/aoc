grid = [l[:-1] for l in open('data')]

p = None

for x,v in enumerate(grid[0]):
    if v == '|':
        p = x,0

ds = ((0,1),(1,0),(0,-1),(-1,0))

d = 0

def get(p,d):
    nd = ds[d]
    return p[0]+nd[0],p[1]+nd[1]

s = ''
while True:

    nnp = None
    for nd in (0,1,3):
        dd = (d + nd)%4
        np = get(p,dd)

        if np[0] < 0 or np[0] >= len(grid[0]) or np[1] < 0 or np[1] >= len(grid):
            continue

        if grid[np[1]][np[0]].strip():
            nnp = np
            d = dd
            break

    if not nnp:
        break

    p = nnp

    if grid[p[1]][p[0]].isalpha():
        s += grid[p[1]][p[0]]

print(s)


