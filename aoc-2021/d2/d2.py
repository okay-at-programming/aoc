x = 0
y = 0

for l in open('data'):
    i,d = l.split(' ')
    if i == 'forward':
        x += int(d)
    if i == 'down':
        y += int(d)
    if i == 'up':
        y -= int(d)

print(x,y,x*y)
