loop = 1

c = 0
n = 0

for i in range(50000000):
    c = (c+349)%loop

    if c == 0:
        n = i+1
    loop += 1
    c += 1


print(n)
