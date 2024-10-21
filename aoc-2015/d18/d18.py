grid = set()

y = 0
for l in open('data'):
    x = 0
    for c in l:
        if c == '#':
            grid.add((x,y))
        x += 1
    y += 1

grid_size = y

def print_grid():
    for y in range(grid_size):
        s = ''
        for x in range(grid_size):
            s += '#' if (x,y) in grid else '.'
        print(s)


for i in range(100):
    new_grid = set()

    for y in range(grid_size):
        for x in range(grid_size):

            n = 0
            for dx,dy in ((0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)):
                if (x+dx,y+dy) in grid:
                    n += 1
            if (x,y) in grid and n in (2,3):
                new_grid.add((x,y))
            elif (x,y) not in grid and n == 3:
                new_grid.add((x,y))

    grid = new_grid

print(len(grid))
