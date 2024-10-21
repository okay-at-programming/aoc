
grid = []
points = set()

def getpoints(p1, p2):
  ip = set()
  for p in points:
    if p[0] <= max(p1[0],p2[0]) and p[0] >= min(p1[0],p2[0]) and p[1] <= max(p1[1],p2[1]) and p[1] >= min(p1[1],p2[1]):
      ip.add(p)
  return ip
  
def getline(p1,p2):
  a = p2[1] - p1[1]
  b = p1[0] - p2[0]
  c = a*p1[0] + b*p1[1]
  
  return a,b,c

y = 0
for line in open('test.txt', 'r'):
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
  


mv = 0
mp = None
for p1 in points:
  count = 0
  for p2 in points:
    if p1 == p2:
      continue
      
    a,b,c = getline(p1,p2)
    
    visible = True
    for p in getpoints(p1, p2):
      if a*p[1] + b*p[0] == c:
        visible = False
        continue
    
    if visible:
      count += 1
  if count > mv:
    mv = count
    mp = p1
print(mv)
print(mp)