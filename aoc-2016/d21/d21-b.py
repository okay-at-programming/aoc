

def swappos(s,x,y):
    if y < x:
        x,y = y,x
    return s[:x] + s[y] + s[x+1:y] + s[x] + s[y+1:]

def swaplet(s,x,y):
    s = s.replace(x,'#')
    s = s.replace(y, x)
    return s.replace('#', y)

def rotatelr(s,d,x):
    if d == 'left':
        return s[x:] + s[:x]
    return s[-x:] + s[:-x]

def rotatepos(s,x):
    i = s.find(x) + 1
    if i >= 5:
        i += 1
    i = i%len(s)
    return rotatelr(s,'right',i)

def revrotatepos(s,x):
    i = s.find(x)
    if i%2 == 1:
        return rotatelr(s,'left',((i-1)//2)+1)
    elif i > 0:
        return rotatelr(s, 'left', ((i//2)+5)%len(s))
    return rotatelr(s,'right',7)

def reverse(s,x,y):
    if y < x:
        x,y = y,x

    return s[:x] + s[x:y+1][::-1] + s[y+1:]

def move(s,x,y):
    if x < y:
        return s[:x] + s[x+1:y+1] + s[x] + s[y+1:]
    return s[:y] + s[x] + s[y:x] + s[x+1:]

s = 'fbgdceah'
steps = [l.strip() for l in open('data')]
for l in steps[::-1]:
    print(l)
    ws = l.split()
    if ws[0] == 'swap' and ws[1] == 'position':
        s = swappos(s,int(ws[2]),int(ws[5]))
    elif ws[0] == 'swap' and ws[1] == 'letter':
        s = swaplet(s,ws[2],ws[5])
    elif ws[0] == 'rotate' and ws[1] == 'based':
        s = revrotatepos(s,ws[6])
    elif ws[0] == 'rotate':
        s = rotatelr(s,'right' if ws[1] == 'left' else 'left',int(ws[2]))
    elif ws[0] == 'reverse':
        s = reverse(s,int(ws[2]),int(ws[4]))
    elif ws[0] == 'move':
        s = move(s, int(ws[5]),int(ws[2]))
    else:
        assert False
    print(s)

print(s)
