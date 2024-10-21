grid = set()

for l in open('data'):
    l = l.strip()
    on = l.split()[0] == 'on'
    c = []
    for x in l.split()[1].split(','):
        c.extend([int(x) for x in x.split('=')[1].split('..')])

    for x in range(max(c[0],-50),min(c[1]+1,51)):
        for y in range(max(c[2],-50),min(c[3]+1,51)):
            for z in range(max(c[4],-50),min(c[5]+1,51)):
                if on:
                    grid.add((x,y,z))
                else:
                    grid.discard((x,y,z))

print(len(grid))
