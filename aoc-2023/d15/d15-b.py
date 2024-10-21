
def hsh(s):
    r = 0
    for c in s:
        r += ord(c)
        r = (r*17)%256
    return r

def indx(l,k):
    for i, (a,b) in enumerate(l):
        if a == k:
            return i
    return -1


boxes = {k:[] for k in range(256)}

for g in open('data').read().strip().split(','):
    if '-' in g:
        l = g.split('-')[0]
        bk = hsh(l)
        i = indx(boxes[bk], l)
        if i >= 0:
            boxes[bk].pop(i)
    elif '=' in g:
        l = g.split('=')[0]
        fl = int(g.split('=')[1])
        bk = hsh(l)
        i = indx(boxes[bk], l)
        if i >= 0:
            boxes[bk][i] = l,fl
        else:
            boxes[bk].append((l,fl))
    else:
        assert False

fp = 0
for k,v in boxes.items():
    for i,(l,p) in enumerate(v):
        fp += (k+1)*(i+1)*p
print(fp)
