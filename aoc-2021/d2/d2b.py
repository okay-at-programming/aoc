x = 0
y = 0
a = 0

for l in open('data'):
    i,d = l.split(' ')
    d = int(d)
    if i == 'forward':
        x += d
        y += a*d
    if i == 'down':
        a += d
    if i == 'up':
        a -= d

print(x,y,x*y)
