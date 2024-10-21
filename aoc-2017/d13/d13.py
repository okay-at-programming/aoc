i = 0

s = 0
for line in open('data'):
    i = int(line.split(':')[0])
    j = int(line.split()[1])
    k = (j-1)*2

    if i%k == 0:
        s += i*j
print(s)

