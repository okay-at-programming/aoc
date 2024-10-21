
l = 5
g = set()
for i in range(l):
    g.add(i)

def plus(i, d=1):
    return (i+d)%l

def minus(i):
    return (i-1)%l

def next(i):
    j = plus(i)
    while True:
        if j in g:
            return j
        j = plus(j)

def last(i):
    j = minus(i)
    while True:
        if j in g:
            return j
        j = minus(j)

def middle(a,b):
    if b < a:
        b += l

    return ((a+b)//2)%l

def opp(i):
    a = plus(i)
    b = minus(i)
    m = middle(a,b)

    if a < m:
        s = len({x for x in g if a <= x <= m})
    else:
        s = len({x for x in g if a <= x or x <= m})

    d = len(g)//2 - s


i = 0

while len(g) > 1:
    j = opp(i)
    g.remove(j)
    i = next(i)


print(g)
