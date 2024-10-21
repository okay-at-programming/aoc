

def pap(s):
    x,y,z = [int(w) for w in s.split('x')]

    tot = 2 * x * y + 2 * y * z + 2 * z * x

    ex = sorted((x,y,z))[:2]

    return tot + ex[0]*ex[1]

t = 0
for l in open('data'):
    t += pap(l.strip())

print(t)
