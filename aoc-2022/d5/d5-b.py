d = open('data').read()

t,b = d.split('\n\n')


t = t.split('\n')
i = len(t)-1
cind = {}
for j in range(len(t[i])):
    if t[i][j] != ' ':
        cind[t[i][j]] = j
print(cind)
ccount = len([x for x in t[i] if x != ' '])
print(ccount)
ss = {}
i -= 1
while i >= 0:
    for j in range(ccount):
        k = 1 + 4*j
        c = t[i][k]
        if c == ' ':
            continue

        jc = str(j+1)
        if jc not in ss:
            ss[jc] = []
        ss[jc].append(c)
    i -= 1


print(ss)

for l in b.split('\n'):
    if not l:
        continue
    l = l.split()
    c,a,b = l[1],l[3],l[5]
    c = int(c)

    ss[b].extend(ss[a][-c:])

    for _ in range(c):
        d = ss[a].pop(-1)


print(ss)
s = ''
for j in range(ccount):
    s += ss[str(j+1)][-1]
print(s)
