
l = 3001330
g = set()
for i in range(l):
    g.add(i)

def plus(i):
    return (i+1)%l

def next(i):
    j = plus(i)
    while True:
        if j in g:
            return j
        j = plus(j)

i = 0

while len(g) > 1:
    j = next(i)
    g.remove(j)
    i = next(j)


print(g)
