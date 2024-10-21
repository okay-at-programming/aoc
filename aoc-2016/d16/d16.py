
def fill(s):
    ns = '0'
    for i in range(len(s)-1,-1,-1):
        ns = s[i] + ns + ('1' if s[i] == '0' else '0')
    return ns

def fillup(s, size):
    ns = fill(s)
    while len(ns) < size:
        print(len(ns),size)
        ns = fill(ns)
    return ns[:size]

def check(s):
    cs = ''
    for i in range(0,len(s)-1,2):
        cs += '1' if s[i] == s[i+1] else '0'
    return cs

def checksum(s):
    cs = check(s)
    while len(cs)%2 == 0:
        cs = check(cs)
    return cs

size = 35651584
state = '01111010110010011'

print(checksum(fillup(state, size)))
