from collections import deque

maze = [list(line[:-1]) for line in open('data')]

def outer(p):
  return p[0] == 2 or p[1] == 2 or p[0] == len(maze[0])-3 or p[1] == len(maze)-3

start = None
end = None
ps = {}
portals = {}
for y in range(len(maze)):
  for x in range(len(maze[y])):
    if maze[y][x].isupper():
      l = x,y
      n = None
      m = None
      a = maze[y][x]
      b = None
      if y+1 < len(maze) and maze[y+1][x].isupper():
        n = x,y+1
        if y+2 < len(maze) and maze[y+2][x] == '.':
          m = x,y+2
        elif y-1 >= 0 and maze[y-1][x] == '.':
          m = x,y-1
      elif x+1 < len(maze[y]) and maze[y][x+1].isupper():
        n = x+1,y
        if x+2 < len(maze[y]) and maze[y][x+2] == '.':
          m = x+2,y
        elif x-1 >= 0 and maze[y][x-1] == '.':
          m = x-1,y
      else:
        continue

      a = maze[l[1]][l[0]]
      b = maze[n[1]][n[0]]

      if a+b == 'AA':
        start = m,0
      elif a+b == 'ZZ':
        end = m,0
      elif (a,b) in ps:
        i = 1 if outer(m) else -1
        portals[ps[a,b]] = m,i
        portals[m] = ps[a,b],-i
      else:
        ps[a,b] = m


visited = set()
queue = deque()
queue.append((start,0))
d = 0

while len(queue) > 0:
  t,c = queue.popleft()
  p,l = t

  if t == end:
    print(c)
    break
  elif t in visited:
    continue

  visited.add(t)

  if p in portals:
    if (l == 0 and portals[p][1] > 0) or l > 0:
      queue.append(((portals[p][0],portals[p][1]+l),c+1))
  if maze[p[1]+1][p[0]] == '.':
    queue.append((((p[0],p[1]+1),l),c+1))
  if maze[p[1]][p[0]+1] == '.':
    queue.append((((p[0]+1,p[1]),l),c+1))
  if maze[p[1]-1][p[0]] == '.':
    queue.append((((p[0],p[1]-1),l),c+1))
  if maze[p[1]][p[0]-1] == '.':
    queue.append((((p[0]-1,p[1]),l),c+1))

  if l > d:
    d = l
    print(d,len(queue))
