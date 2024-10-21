from collections import deque

reg = open('data').read().strip()

map = {}
map[(0,0)] = 'X'

def route(path, pos):
    if len(path) == 0:
        return
    i = 0
    s = ''
    while True:
        if path[i] == '(':
            break

        x,y = pos
        if path[i] == 'E':
            map[(x+1,y)] = '|'
            pos = x+2,y
        if path[i] == 'S':
            map[(x,y+1)] = '-'
            pos = x,y+2
        if path[i] == 'W':
            map[(x-1,y)] = '|'
            pos = x-2,y
        if path[i] == 'N':
            map[(x,y-1)] = '-'
            pos = x,y-2
        map[pos] = '.'

        s += path[i]
        i += 1
        if i >= len(path):
            return
    if path[i] == '(':
        j = i+1
        k = 0
        while True:
            if path[j] == ')' and k == 0:
                route(path[i+1:j], pos)
                break
            if path[j] == '|' and k == 0:
                route(path[i+1:j], pos)
                i = j
            if path[j] == '(':
                k += 1
            if path[j] == ')':
                k -= 1
            j += 1
    route(path[j+1:], pos)



route(reg[1:-1], (0,0))

xmin, xmax,ymin,ymax = 0,0,0,0

for x,y in map.keys():
    if x < xmin: xmin = x
    if x > xmax: xmax = x
    if y < ymin: ymin = y
    if y > ymax: ymax = y


for y in range(ymin-1, ymax+2):
    s = ''
    for x in range(xmin-1, xmax+2):
        s += map.get((x,y), '#')

    print(s)


vis = set()

q = deque()
q.append(((0,0),0))
far = set()

while len(q) > 0:
    pos, doors = q.pop()

    if pos in vis:
        continue
    vis.add(pos)

    if doors >= 1000:
        far.add(pos)

    x,y = pos

    for dx,dy in ((1,0), (0,1), (-1,0), (0,-1)):
        if (x+dx,y+dy) in map:
            q.append(((x+2*dx,y+2*dy),doors+1))

print(len(far))
