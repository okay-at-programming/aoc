coords = set()
folds = []

fs = False

for l in open('data'):
    if not l.strip():
        fs = True
        continue
    if not fs:
        x,y = [int(x) for x in l.strip().split(',')]
        coords.add((x,y))
    else:
        v = l.strip().split()[-1]
        x,y = v.split('=')
        folds.append((x,int(y)))


for ax,m in folds[:1]:
    nc = set()
    for x,y in coords:
        nx,ny = x,y
        if ax == 'x' and x > m:
            nx = 2*m-x
        elif ax == 'y' and y > m:
            ny = 2*m-y
        nc.add((nx,ny))
    coords = nc

print(len(coords))

