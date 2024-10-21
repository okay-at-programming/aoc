total = 0

for l in open('data'):
    l = l.strip()
    fl = len(l)
    c,i = 2,0
    while i < len(l):
        if l[i] == '\\' or l[i] == '"':
            c += 2
        else:
            c += 1
        i += 1
    print(l, c, fl)
    total += (c - fl)
print(total)
