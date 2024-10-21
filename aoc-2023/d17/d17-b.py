from queue import PriorityQueue

g =[l.strip() for l in open('data')]

t = len(g[0])-1, len(g)-1

q = PriorityQueue()
q.put((-int(g[0][0]),0,0,0,-1))
q.put((-int(g[0][0]),0,0,1,-1))


def val(x,y):
  return 0<=x<len(g[0]) and 0<=y<len(g)

dirs = ((1,0),(0,1),(-1,0),(0,-1))

seen = {}

while q:
  hl,x,y,d,ds = q.get()

  hl = hl + int(g[y][x])
  if (x,y)==t and ds>=3:
      print(hl)
      break

  shl = seen.get((x,y,d,ds))

  if shl and hl>=shl:
    continue

  seen[(x,y,d,ds)] = hl

  if ds<9:
    nx,ny = x+dirs[d][0],y+dirs[d][1]
    if val(nx,ny):
      q.put((hl,nx,ny,d,ds+1))

  if ds >=3:
    for ods in ((d+1)%4,(d+3)%4):
      nx,ny = x+dirs[ods][0],y+dirs[ods][1]
      if val(nx,ny):
        q.put((hl,nx,ny,ods,0))


