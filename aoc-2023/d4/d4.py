
t = 0
for l in open('data'):
    w = l.split(':')[1].split('|')[0].strip().split()
    y = l.split(':')[1].split('|')[1].strip().split()

    w = set(map(int, w))
    y = set(map(int, y))

    s = w.intersection(y)

    p = 1 if len(s) >= 1 else 0

    if len(s) > 1:
        p = p*(2**(len(s)-1))

    t += p

    print(t)

print(t)
