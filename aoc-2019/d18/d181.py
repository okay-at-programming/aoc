from collections import deque

maze = [list(line.strip()) for line in open('data')]

class route:
  def __init__(self, x, y, visited, got, steps, r):
    self.x = x
    self.y = y
    self.visited = visited
    self.got = got
    self.steps = steps
    self.r = r

  def copy(self,dx,dy):
    return route(self.x+dx,self.y+dy, self.visited.copy(), self.got.copy(), self.steps + 1, self.r)

  def visit(self, dx, dy):
    point = self.x+dx, self.y+dy
    return point not in self.visited or len(self.got) > self.visited[point]

keys = set()
doors = set()
point = None
for y in range(len(maze)):
  for x in range(len(maze[y])):
    if maze[y][x] == '@':
      point = x,y
      maze[y][x] = '.'
    elif maze[y][x].isupper():
      doors.add(maze[y][x])
    elif maze[y][x].islower():
      keys.add(maze[y][x])

queue = deque()
queue.append(route(point[0],point[1],{},set(),0,''))
m = 0
best = set()

while len(queue) > 0:
  current = queue.popleft()

  point = current.x, current.y
  if (point,current.r) in best:
    continue
  spot = maze[current.y][current.x]
  if spot.isupper() and spot.lower() not in current.got:
    continue
  elif spot.islower() and spot not in current.got:
    current.got.add(spot)
    current.r += spot

  best.add((point,current.r))

  current.visited[point] = len(current.got)

  if len(current.got) == len(keys):
    print(current.steps)
    break

  if current.visit(1,0) and maze[current.y][current.x+1] != '#':
    queue.append(current.copy(1,0))
  if current.visit(0,1) and maze[current.y+1][current.x] != '#':
    queue.append(current.copy(0,1))
  if current.visit(-1,0) and maze[current.y][current.x-1] != '#':
    queue.append(current.copy(-1,0))
  if current.visit(0,-1) and maze[current.y-1][current.x] != '#':
    queue.append(current.copy(0,-1))

  if len(current.got) > m:
    m = len(current.got)
    print(m, current.steps, current.r)
  if len(queue)%10000 == 0:
    print(len(queue))



