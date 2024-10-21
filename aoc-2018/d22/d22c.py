from queue import PriorityQueue

#depth = 510
#target = 10,10
depth = 4002
target = 5,746

top = 1000

grid = [[None for _ in range(target[1]+top)] for _ in range(target[0]+top)]
paths = [[None for _ in range(target[1]+top)] for _ in range(target[0]+top)]

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

for y in range(0,target[1]+top):
    for x in range(0,target[0]+top):
        el = ero(x,y)
        t = el%3
        paths[x][y] = t

for r in paths:
    s = ''
    for c in r:
        s += str(c)
    #print(s)

# x,y,steps,equiped
q = PriorityQueue()
q.put((0,0,0,1))
seen = set()
target = target[0],target[1],1

while not q.empty():
     steps,x,y,equipped = q.get()

     if equipped == paths[x][y]:
         continue

     if (x,y,equipped) == target:
         print(steps)
         break

     if (x,y,equipped) in seen:
         continue

     seen.add((x,y,equipped))

     for i in range(3):
         diff = 1 if i == equipped else 8

         if i == paths[x][y]:
             continue

         for nx,ny in ((x+1,y),(x,y+1),(x-1,y),(x,y-1)):
             if nx < 0 or ny < 0 or nx >= target[0]+top or ny >= target[1]+top:
                 continue
             q.put((steps+diff,nx,ny,i))

