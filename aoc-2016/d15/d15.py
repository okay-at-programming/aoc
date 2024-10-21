disks = []

for l in open('data2'):
    x = int(l.split()[3])
    y = int(l.split()[-1][:-1])
    disks.append((x,y))

success = False
t = 0
while not success:
    success = True
    di = 1
    for d in disks:
        s = (t + di + d[1]) % d[0]
        if s != 0:
            success = False
            t += 1
            break
        di += 1

print(t)
