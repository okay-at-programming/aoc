data = {int(line.split(':')[0]):int(line.split()[1]) for line in open('data')}

i = 0
d = 0
while True:
    f = True
    for i in data.keys():
        j = data[i]
        i += d
        k = (j-1)*2

        if i%k == 0:
            f = False
            break
    if f:
        print(d)
        break
    d += 1

