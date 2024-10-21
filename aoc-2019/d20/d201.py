from collections import deque

maze = [list(line[:-1]) for line in open('data')]

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
        start = m
      elif a+b == 'ZZ':
        end = m
      elif (a,b) in ps:
        portals[ps[a,b]] = m
        portals[m] = ps[a,b]
      else:
        ps[a,b] = m


visited = set()
queue = deque()
queue.append((start,0))

while len(queue) > 0:
  p,c = queue.popleft()

  if p == end:
    print(c)
    break
  elif p in visited:
    continue

  visited.add(p)

  if p in portals:
    queue.append((portals[p],c+1))
  if maze[p[1]+1][p[0]] == '.':
    queue.append(((p[0],p[1]+1),c+1))
  if maze[p[1]][p[0]+1] == '.':
    queue.append(((p[0]+1,p[1]),c+1))
  if maze[p[1]-1][p[0]] == '.':
    queue.append(((p[0],p[1]-1),c+1))
  if maze[p[1]][p[0]-1] == '.':
    queue.append(((p[0]-1,p[1]),c+1))




