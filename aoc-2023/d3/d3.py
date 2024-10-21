def symbol(dx, dy):
  if 0<=dx<len(g[0]) and 0<=dy<len(g):
    c = g[dy][dx]
    return not (c.isdigit() or c=='.')

g = [l.strip() for l in open('data')]
ignore = True
d=0
total = 0

for y,l in enumerate(g):
  if d:
    if not ignore:
      total += d
    d=0
    ignore = True

  x = 0
  for c in l:
    if c.isdigit():
      if not d:
        for dx, dy in ((x-1,y-1),(x-1,y),(x-1,y+1)):
          if symbol(dx,dy):
            ignore = False
      d = 10*d + int(c)
      for dx, dy in ((x,y-1),(x,y+1)):
        if symbol(dx,dy):
          ignore = False
    else:
       if d:
         for dx, dy in ((x,y-1),(x,y),(x,y+1)):
           if symbol(dx,dy):
             ignore = False
         if not ignore:
           total += d
         d=0
         ignore = True
    x+=1

if d and not ignore:
  total += d

print(total)
