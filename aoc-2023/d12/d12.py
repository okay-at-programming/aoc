
def f(p,m,c):
    if len(p) == len(m):
        r = [str(len(x)) for x in p.split('.') if x]
        s = ','.join(r)
        if s == c:
            return 1
        return 0

    i = len(p)
    if m[i] in '.#':
        return f(p + m[i],m,c)

    r = 0
    r += f(p+'.',m,c)
    r += f(p+'#',m,c)

    return r

t = 0
for l in open('data'):
    m,c = l.strip().split()
    r = f('',m,c)
    t += r

print(t)
