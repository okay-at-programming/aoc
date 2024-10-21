
def hsh(s):
    r = 0
    for c in s:
        r += ord(c)
        r = (r*17)%256
    return r


t = 0
for g in open('data').read().strip().split(','):
    t += hsh(g)
print(t)
