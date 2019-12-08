data = []
for line in open('data.txt', 'r'):
  line = line.strip()
  data.append(line.split(')'))

do = {}
for d in data:
  if d[1] not in do:
    do[d[1]] = []
  if d[0] not in do:
    do[d[0]] = []
  do[d[1]].append(d[0])

def co(p,c):
  c += len(do[p])
  for d in do[p]:
    c = co(d,c)
  return c

count = 0
for p, o in do.items():
  count = co(p,count)

print(count)