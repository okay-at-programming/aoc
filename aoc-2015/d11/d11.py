def gen(s):
    l = [ord(x) for x in s]

    while True:
        i = len(l)-1
        while i >= 0:
            l[i] += 1
            if l[i] > 122:
                l[i] = 97
                i -= 1
            else:
                break
        yield l




def valid(l):
    if 105 in l or 111 in l or 108 in l:
        return False

    ps = 0
    o = -1
    i = 0
    while i < len(l)-1:
        if l[i] == l[i+1] and l[i] != o:
            ps += 1
            o = l[i]
            i += 1
        i += 1
    if ps < 2:
        return False

    for i in range(len(l)-2):
        if l[i] + 1 == l[i+1] and l[i+1] + 1 == l[i+2]:
            return True
    return False


i = 0
for l in gen('vzbxkghb'):
    if valid(l):
        print(''.join([chr(x) for x in l]))
        i += 1
        if i > 1:
            break


