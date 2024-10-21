def symbol(dx, dy):
  if 0<=dx<len(g[0]) and 0<=dy<len(g):
    c = g[dy][dx]
    return not (c.isdigit() or c=='.')

g = [l.strip() for l in open('data')]
m ={}
s = set()
d=0
total = 0

for y,l in enumerate(g):
  if d:
    if d in m:
      assert False
    m[(d,x,y)] = s
    d=0
    s = set()
    
  x = 0
  for c in l:
    if c.isdigit():
      if not d:
        for dx, dy in ((x-1,y-1),(x-1,y),(x-1,y+1)):
          if symbol(dx,dy):
            s.add((dx,dy))
      d = 10*d + int(c)
      for dx, dy in ((x,y-1),(x,y+1)):
        if symbol(dx,dy):
          s.add((dx,dy))
    else:
       if d:
         for dx, dy in ((x,y-1),(x,y),(x,y+1)):
           if symbol(dx,dy):
             s.add((dx,dy))
         if d in m:
           assert False
         m[(d,x,y)] = s
         d=0
         s = set()
    x+=1
    
if d:
  if d in m:
    assert False
  m[(d,x,y)] = s
  
for k,v in m.items():
  for ok,ov in m.items():
    if k != ok and k[0]<ok[0]:
      for p in v:
        for op in ov:
          if p==op:
            total += k[0]*ok[0]
  
print(total)