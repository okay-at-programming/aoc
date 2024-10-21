cons = (20, 15, 10, 5, 5)
cons = tuple([int(i) for i in open('data')])

def ways(c, l):
    if l == 0:
        return 1
    elif l < 0 or not c:
        return 0

    t = 0
    for i in range(len(c)):
        t += ways(c[i+1:], l-c[i])
    return t

print(ways(cons, 150))

