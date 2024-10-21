
def findend(s):
    i = 1
    p = 1
    while i < len(s):
        if s[i] == ']':
            p -= 1
        elif s[i] == '[':
            p += 1
        if p == 0:
            break
        i += 1
    return i

def comp(r,l):
    if r == l:
        return 0
    if not r and l:
        return 1
    if not l:
        return 2

    if r[0].isnumeric() and l[0].isnumeric():
        rs = r.split(',')
        ls = l.split(',')
        r0 = int(rs[0])
        l0 = int(ls[0])
        if r0 == l0:
            return comp(','.join(rs[1:]),','.join(ls[1:]))
        if r0 < l0:
            return 1
        return 2

    if r[0] == '[' and l[0] == '[':
        re = findend(r)
        le = findend(l)
        a = comp(r[1:re], l[1:le])
        if a != 0:
            return a
        return comp(r[re+2:],l[le+2:])

    if r[0].isnumeric():
        rs = r.split(',')
        rn = '[' + rs[0] + '],' + ','.join(rs[1:])
        return comp(rn,l)

    if l[0].isnumeric():
        ls = l.split(',')
        ln = '[' + ls[0] + '],' + ','.join(ls[1:])
        return comp(r,ln)

    assert False


m = []

for l in open('data2'):
    l = l.strip()
    if not l:
        continue
    i = 0
    d = False
    while i < len(m):
        if comp(l,m[i]) <=1:
            m.insert(i,l)
            d = True
            break
        i += 1
    if not d:
        m.append(l)

t = 1
i = 1
for e in m:
    if e in ('[[2]]','[[6]]'):
        t *= i
    i += 1
print(t)
