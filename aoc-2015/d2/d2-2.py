

def pap(s):
    x,y,z = [int(w) for w in s.split('x')]

    ex = sorted((x,y,z))[:2]

    return x*y*z + 2*ex[0] + 2*ex[1]

print(pap("2x3x4"))
print(pap("1x1x10"))

t = 0
for l in open('data'):
    t += pap(l.strip())

print(t)
