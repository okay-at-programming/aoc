from collections import deque

maze = [list(line.strip()) for line in open('data2')]

class route:
  def __init__(self, p, got, steps, r):
    self.p = p
    self.got = got
    self.steps = steps
    self.r = r

  def copy(self,dx,dy,l):
    p2 = []
    for i in range(4):
      if i == l:
        p2.append((self.p[i][0]+dx,self.p[i][1]+dy))
      else:
        p2.append(self.p[i])
    return route(tuple(p2),self.got.copy(), self.steps + 1, self.r)

keys = set()
s = []
for y in range(len(maze)):
  for x in range(len(maze[y])):
    if maze[y][x] == '@':
      s.append((x,y))
      maze[y][x] = '.'
    elif maze[y][x].islower():
      keys.add(maze[y][x])
    elif maze[y][x] == '.':
      n = maze[y-1][x] + maze[y][x-1] + maze[y+1][x] + maze[y][x+1]
      if '###.' == ''.join(sorted(n)):
        maze[y][x] = '#'

queue = deque()
best = []
for i in range(4):
  queue.append((route(tuple(s),set(),0,''),i))
  best.append(set())
m = 0

while len(queue) > 0:
  current,l = queue.popleft()

  point = current.p[l]
  if (point,current.r) in best[l]:
    continue
  spot = maze[point[1]][point[0]]
  if spot.isupper() and spot.lower() not in current.got:
    continue
  elif spot.islower() and spot not in current.got:
    current.got.add(spot)
    current.r = ''.join(sorted(current.r + spot))

  best[l].add((point,current.r))

  if len(current.got) == len(keys):
    print(current.steps)
    break

  for i in range(4):
    if maze[current.p[i][1]][current.p[i][0]+1] != '#':
      queue.append((current.copy(1,0,i), i))
    if maze[current.p[i][1]+1][current.p[i][0]] != '#':
      queue.append((current.copy(0,1,i), i))
    if maze[current.p[i][1]][current.p[i][0]-1] != '#':
      queue.append((current.copy(-1,0,i), i))
    if maze[current.p[i][1]-1][current.p[i][0]] != '#':
      queue.append((current.copy(0,-1,i), i))

  if len(current.got) > m:
    m = len(current.got)
    print(m, current.steps, current.r)



