t = 0

for l in open('data'):
    f = None
    e = None
    for c in l:
        if c.isdigit():
            if not f:
                f = c
            e = c
    t += int(f+e)

print(t)
