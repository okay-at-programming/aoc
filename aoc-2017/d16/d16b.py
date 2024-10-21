f = []

dance = open('data').read().strip().split(',')

b = 1000000000

for i in range(16):
    c = chr(ord('a') + i)
    f.append(c)

def spin(l, i):
    i *= -1
    l = l[i:] + l[:i]
    return l

def ex(l, a, b):
    l[a],l[b] = l[b],l[a]
    return l

def p(l, a, b):
    a,b = l.index(a), l.index(b)
    return ex(l,a,b)

ls = 30
t = b%ls

for n in range(t):
    for i in dance:
        if i[0] == 's':
            j = int(i[1:])
            f = spin(f,j)
        elif i[0] == 'x':
            j,k = [int(x) for x in i[1:].split('/')]
            f = ex(f, j, k)
        elif i[0] == 'p':
            j,k = [x for x in i[1:].split('/')]
            f = p(f, j, k)

print(''.join(f))
