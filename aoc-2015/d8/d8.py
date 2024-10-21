total = 0

for l in open('data'):
#for l in ('""', '"abc"', '"aaa\\"aaa"', '"\\x27"'):
    l = l.strip()[1:-1]
    fl = len(l) + 2
    c,i = 0,0
    while i < len(l):
        if l[i] == '\\':
            if l[i+1] == '\\' or l[i+1] == '"':
                i += 2
                c += 1
            elif l[i+1] == 'x':
                i += 4
                c += 1
            else:
                assert False
        else:
            i += 1
            c += 1
    total += (fl - c)
print(total)
