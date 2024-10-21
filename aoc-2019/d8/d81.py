data = open('data.txt', 'r').read()

layer = 25*6

minzero = 100000000000000000
minz = 0
ocount = 0
tcount = 0
zount = 0

i = 0
for c in data:
  if c == '0':
    zount += 1
  elif c == '1':
    ocount += 1
  elif c == '2':
    tcount += 1
  
  i += 1
  
  if i == layer:
    if zount < minzero:
      minz = ocount*tcount
      minzero = zount
    i = 0
    zount = 0
    ocount = 0
    tcount = 0

print(minz)
