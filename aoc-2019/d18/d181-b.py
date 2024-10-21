from collections import deque

maze = [list(line.strip()) for line in open('data')]

class route:
  def __init__(self, x, y, got, steps, r):
    self.x = x
    self.y = y
    self.got = got
    self.steps = steps
    self.r = r

  def copy(self,dx,dy):
    return route(self.x+dx,self.y+dy, self.got.copy(), self.steps + 1, self.r)

keys = set()
point = None
for y in range(len(maze)):
  for x in range(len(maze[y])):
    if maze[y][x] == '@':
      point = x,y
      maze[y][x] = '.'
    elif maze[y][x].islower():
      keys.add(maze[y][x])


n = 0,-1
e = 1,0
s = 0,1
w = -1,0

queue = deque()
queue.append((route(point[0],point[1],set(),0,''),(0,0)))
m = 0
best = set()

while len(queue) > 0:
  current,prev = queue.popleft()
  active = False

  point = current.x, current.y
  if (point,current.r) in best:
    continue
  spot = maze[current.y][current.x]
  if spot.isupper() and spot.lower() not in current.got:
    continue
  elif spot.islower() and spot not in current.got:
    active = True
    current.got.add(spot)
    current.r = ''.join(sorted(current.r + spot))

  best.add((point,current.r))

  if len(current.got) == len(keys):
    print(current.steps)
    break

  if (prev != e or active) and maze[current.y][current.x+1] != '#':
    queue.append((current.copy(1,0), w))
  if (prev != s or active) and maze[current.y+1][current.x] != '#':
    queue.append((current.copy(0,1), n))
  if (prev != w or active) and maze[current.y][current.x-1] != '#':
    queue.append((current.copy(-1,0), e))
  if (prev != n or active) and maze[current.y-1][current.x] != '#':
    queue.append((current.copy(0,-1), s))

  if len(current.got) > m:
    m = len(current.got)
    print(m, current.steps, current.r)
  if len(queue)%10000 == 0:
    print(len(queue))



