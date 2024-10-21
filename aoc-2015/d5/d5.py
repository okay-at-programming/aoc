t = 0

for l in open('data'):
    if 'ab' in l or 'cd' in l or 'pq' in l or 'xy' in l:
        continue

    dub = False
    prev = None
    vc = 0

    for c in l:
        if c in 'aeiou':
            vc += 1
        if c == prev:
            dub = True
        prev = c

    if dub and vc >= 3:
        t += 1

print(t)
