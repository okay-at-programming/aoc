from collections import deque

depth = 510
target = 10,10

top = 10

grid = [[None for _ in range(target[1]+top)] for _ in range(target[0]+top)]
path = [[None for _ in range(target[1]+top)] for _ in range(target[0]+top)]

def ero(x,y):
    if grid[x][y]:
        return grid[x][y]
    elif (x,y) == (0,0) or (x,y) == target:
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

for y in range(0,target[1]+1):
    for x in range(0,target[0]+1):
        el = ero(x,y)
        t = el%3
        grid[x][y] = t

for row in map:
    s = ''
    for c in row:
        s += str(c)
    print(c)

# x,y,steps,equiped
q = deque()
q.append((0,0,0,1))
seen = {}

while len(q) > 0:
    x,y,steps,equipped = q.pop()

    if (x,y) == target:
        if equipped != 1:
            steps += 7
        print(steps)
        break

    if equipped == map[x][y]:
        continue

    if (x,y) in seen and seen[(x,y)] <= steps:
        continue

    seen[(x,y)] = steps

    for i in range(3):
        diff = 1 if i == equipped else 8

        for nx,ny in ((x+1,y),(x,y+1),(x-1,y),(x,y-1)):
            if nx < 0 or ny < 0 or nx >= target[0]+top or ny >= target[1]+top:
                continue
            q.append((nx,ny,steps+diff,i))



