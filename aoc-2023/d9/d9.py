def f(l):
    if all((x == 0 for x in l)):
        return 0
    r = []
    i = 1
    while i < len(l):
        r.append(l[i] - l[i-1])
        i += 1

    n = f(r)

    return l[-1] + n


t = 0
for l in open('data'):
    l = [int(x) for x in l.split()]

    n = f(l)

    t += n

print(t)

