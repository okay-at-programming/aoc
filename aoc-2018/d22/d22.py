depth = 4002
target = 5,746

grid = [[None for _ in range(target[1]+1)] for _ in range(target[0]+1)]

def ero(x,y):
    if grid[x][y]:
        return grid[x][y]
    elif (x,y) == (0,0):
        geo = 0
    elif y == 0:
        geo = x*16807
    elif x == 0:
        geo = y*48271
    else:
        geo = grid[x-1][y] * grid[x][y-1]
    el = (geo + depth)%20183
    grid[x][y] = el
    return el

types = {0:'.',1:'=',2:'|'}
total = 0
for y in range(0,target[1]+1):
    s = ''
    for x in range(0,target[0]+1):
        if (x,y) == (0,0):
            s += 'M'
            continue
        if (x,y) == target:
            s += 'T'
            continue
        el = ero(x,y)
        t = el%3
        s += types[t]
        total += t
    print(s, y)

print(total)

