g = set()

for l in open('data'):
    l = l.strip().split(' -> ')
    ox,oy = [int(x) for x in l[0].split(',')]
    g.add((ox,oy))
    for d in l[1:]:
        x,y = [int(x) for x in d.split(',')]
        sx,ex = sorted([x,ox])
        sy,ey = sorted([y,oy])
        for nx in range(sx,ex+1):
            for ny in range(sy,ey+1):
                g.add((nx,ny))
        ox,oy = x,y

def print_g():
    mix = min([x for (x,y) in g])
    miy = min([y for (x,y) in g])
    maxx = max([x for (x,y) in g])
    mayy = max([y for (x,y) in g])

    for y in range(miy,mayy+1):
        s = ''
        for x in range(mix,maxx+1):
            if (x,y) in g:
                s += '#'
            else:
                s += ' '
        print(s)


S = 500,0
mix = min([x for (x,y) in g])
miy = min([y for (x,y) in g])
maxx = max([x for (x,y) in g])
mayy = max([y for (x,y) in g])
sand = set()

def drip():
    x,y = S

    while True:
        if x < mix or x > maxx or y > mayy:
            return False

        if (x,y+1) not in sand and (x,y+1) not in g:
            y += 1
        elif (x-1,y+1) not in sand and (x-1,y+1) not in g:
            x-=1
            y+=1
        elif (x+1,y+1) not in sand and (x+1,y+1) not in g:
            x += 1
            y += 1
        else:
            sand.add((x,y))
            return True

while drip():
    continue

print(len(sand))



