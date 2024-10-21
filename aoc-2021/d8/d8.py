t = 0

for l in open('data'):
    sig,out = l.split('|')

    for o in out.strip().split(' '):
        if len(o) in (2,3,4,7):
            t += 1

print(t)


