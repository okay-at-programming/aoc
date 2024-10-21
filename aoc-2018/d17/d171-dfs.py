from collections import deque
import sys

sys.setrecursionlimit(3000)

grid = {}

for line in open('data'):
    a,b = line.split(', ')

    c, d = a.split('=')
    e,f = b.split('=')
    g,h = f.split('..')

    for i in range(int(g), int(h)+1):
        p = None
        if c == 'x':
            p = int(d),i
        else:
            p = i, int(d)
        grid[p] = '#'

minx = None
miny = None
maxx = None
maxy = None

for p in grid.keys():
    if not minx or p[0] < minx:
        minx = p[0]
    if not miny or p[1] < miny:
        miny = p[1]
    if not maxx or p[0] > maxx:
        maxx = p[0]
    if not maxy or p[1] > maxy:
        maxy = p[1]


def wall(grid, pos, d):
    x,y = pos
    while True:
        if (x,y) not in grid:
            return False
        if grid[(x,y)] == '#':
            return True
        x += d

def walled(grid, pos):
    return wall(grid, pos, 1) and wall(grid, pos, -1)

def leveld(grid, pos, d):
    x,y = pos
    while True:
        if grid[(x,y)] == '#':
            return
        grid[(x,y)] = '~'
        x += d

def level(grid, pos):
    leveld(grid, pos, 1)
    leveld(grid, pos, -1)



def fill(grid, pos):
    x,y = pos

    if y > maxy:
        return

    if (x,y+1) not in grid:
        grid[(x,y+1)] = '|'
        fill(grid, (x,y+1))

    if grid.get((x,y+1), ' ') in '#~' and (x+1,y) not in grid:
        grid[(x+1, y)] = '|'
        fill(grid, (x+1,y))

    if grid.get((x,y+1), ' ') in '#~' and (x-1,y) not in grid:
        grid[(x-1,y)] = '|'
        fill(grid, (x-1,y))

    if walled(grid, pos):
        level(grid, pos)

fill(grid, (500,0))

wet = 0
still = 0

for y in range(miny, maxy+1):
    s = ''
    for x in range(minx-1, maxx+2):
        c = grid.get((x,y), ' ')
        if c in '|~':
            wet += 1
        if c == '~':
            still += 1
        s += c

    print(s)

print()
print('a:',wet)
print('b:',still)
