t = 0

for l in open('data'):
#for l in ('qjhvhtzxzqqjkmpb',):
    pair = False
    for i in range(1,len(l)-1):
        if l[i-1] == l[i+1]:
            pair = True
            break

    rep = False
    for i in range(len(l)-1):
        if l[i:i+2] in l[:i] or l[i:i+2] in l[i+2:]:
            rep = True
            break

    if pair and rep:
        t += 1

print(t)
