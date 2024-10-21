t = 0
for l in open('data'):
    e1,e2 = l.split(',')

    e1s,e1e = e1.split('-')
    e2s,e2e = e2.split('-')

    e1s,e1e,e2s,e2e = [int(x) for x in [e1s,e1e,e2s,e2e]]

    if e1s <= e2s and e1e >= e2e:
         t += 1
    elif e2s <= e1s and e2e >= e1e:
         t += 1
    elif e1s <= e2s and e1e >= e2s:
        t += 1
    elif e1s <= e2e and e1e >= e2e:
        t += 1

print(t)
