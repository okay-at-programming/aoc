def say(w):
    i = 0
    r = ''
    while i < len(w):
        c = i
        while c < len(w) and w[c] == w[i]:
            c += 1
        r += str(c-i) + w[i]
        i = c
    return r

w = '1321131112'

for i in range(50):
    w = say(w)
    print(i, len(w))
