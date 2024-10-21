grid = []
points = set()

def getpoints(p1, p2):
  ip = set()
  for p in points:
    if p1 != p and p2 != p and p[0] <= max(p1[0],p2[0]) and p[0] >= min(p1[0],p2[0]) and p[1] <= max(p1[1],p2[1]) and p[1] >= min(p1[1],p2[1]):
      ip.add(p)
  return ip

def getline(p1,p2):
  a = p2[1] - p1[1]
  b = p1[0] - p2[0]
  c = a*p1[0] + b*p1[1]

  return a,b,c


y = 0
for line in open('test', 'r'):
  row = []
  x = 0
  for c in line:
    if c == '.':
      row.append('.')
    elif c == '#':
      row.append('#')
      points.add((x,y))
    x += 1
  grid.append(row)
  y += 1

vps = []
point = 11,13
for p2 in points:
  if point == p2:
    continue

  a,b,c = getline(point,p2)

  visible = True
  for p in getpoints(point, p2):
    if a*p[0] + b*p[1] == c:
      visible = False
      continue

  if visible:
    vps.append(p2)

print(len(vps))

import math

grid = []
points = set()

def getpoints(p1, p2):
  ip = set()
  for p in points:
    if p1 != p and p2 != p and p[0] <= max(p1[0],p2[0]) and p[0] >= min(p1[0],p2[0]) and p[1] <= max(p1[1],p2[1]) and p[1] >= min(p1[1],p2[1]):
      ip.add(p)
  return ip

def getline(p1,p2):
  a = p2[1] - p1[1]
  b = p1[0] - p2[0]
  c = a*p1[0] + b*p1[1]

  return a,b,c


y = 0
for line in open('data', 'r'):
  row = []
  x = 0
  for c in line:
    if c == '.':
      row.append('.')
    elif c == '#':
      row.append('#')
      points.add((x,y))
    x += 1
  grid.append(row)
  y += 1

vps = []
point = 22,28
for p2 in points:
  if point == p2:
    continue

  a,b,c = getline(point,p2)

  visible = True
  for p in getpoints(point, p2):
    if a*p[0] + b*p[1] == c:
      visible = False
      continue

  if visible:
    vps.append(p2)

def angle(p):
  x = p[0] - point[0]
  y = p[1] - point[1]
  return 180 - math.degrees(math.atan2(x,y))

print(point)
vps.sort(key=angle)
for i in range(1,211):
  print(i, str(vps[i-1]), str(angle(vps[i-1])))
