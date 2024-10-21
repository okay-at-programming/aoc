data = []
for line in open('data.txt', 'r'):
  line = line.strip()
  data.append(line.split(')'))

do = {}
for d in data:
  do[d[1]] = d[0]

you = do['YOU']
san = do['SAN']

r = ''
key = 'YOU'
while key in do:
  r += do[key] + '-'
  key = do[key]

print(r)

count = 1
key = san
while key in do:
  i = r.find(do[key])
  if i > 0:
    new = r.count('-', 0, i)
    print(new)
    print(new + count)
    break
  key = do[key]
  count += 1