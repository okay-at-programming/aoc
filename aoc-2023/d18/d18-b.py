
xcoords = set()
ycoords = set()
walls = set()
x,y = 0,0
xcoords.add(0)
ycoords.add(0)

dirs = {0:(1,0),1:(0,1),2:(-1,0),3:(0,-1)}
#dirs = {'R':(1,0),'D':(0,1),'L':(-1,0),'U':(0,-1)}

for l in open('data'):
    s = l.index('#') + 1
    e = l.index(')')
    d = l.strip()[s:e]

    s = int(d[:-1],16)
    d = int(d[-1])

    #d,s,_ = l.split()
    #s = int(s)

    nx,ny = x+s*dirs[d][0],y+s*dirs[d][1]
    xcoords.add(nx)
    ycoords.add(ny)
    walls.add((x,y,nx,ny))
    x,y = nx,ny


def wall(ax,ay,bx,by):
    for cx,cy,dx,dy in walls:
        cx,dx = min(cx,dx),max(cx,dx)
        cy,dy = min(cy,dy),max(cy,dy)
        if cx<=ax<=dx and cx<=bx<=dx and cy<=ay<=dy and cy<=by<=dy:
            return True
    return False


xcols = sorted(list(xcoords))
ycols = sorted(list(ycoords))


g = {}

corns = set()
edges = set()

inside = set()
t = 0
for i in range(len(xcols)-1):
    for j in range(len(ycols)-1):
        ax,ay = xcols[i],ycols[j]
        bx,by = xcols[i+1],ycols[j+1]

        wl = wall(ax,ay,ax,by)
        li = (i-1,j) in inside

        if (li and wl) or (not li and not wl):
            continue

        inside.add((i,j))
        area = (abs(ax-bx)-1)*(abs(ay-by)-1)
        t += area
        corns.add((ax,ay))
        corns.add((bx,ay))
        corns.add((ax,by))
        corns.add((bx,by))
        edges.add((ax,ay,ax,by))
        edges.add((ax,ay,bx,ay))
        edges.add((bx,ay,bx,by))
        edges.add((ax,by,bx,by))

t += len(corns)
for ax,ay,bx,by in edges:
    if bx > ax:
        t += (bx-ax-1)
    else:
        t += (by-ay-1)

print(t)

