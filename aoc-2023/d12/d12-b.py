
def f(s,ls,gl,seen):
    if not s:
        if ls:
            if len(ls) == 1 and ls[0] == gl:
                return 1
            return 0
        elif gl:
            return 0
        return 1

    if (s,ls,gl) in seen:
        return seen[(s,ls,gl)]

    r = 0
    for o in s[0].replace('?','.#'):
        if o == '#':
            r += f(s[1:],ls,gl+1,seen)
        else:
            if gl:
                if ls and gl == ls[0]:
                    r += f(s[1:],ls[1:],0,seen)
            else:
                r += f(s[1:],ls,0,seen)

    seen[(s,ls,gl)] = r
    return r



t = 0
for l in open('data'):
    m,c = l.strip().split()
    c = [int(x) for x in c.split(',')]
    m = '?'.join([m]*5)
    c = tuple(c*5)
    r = f(m,c,0,{})
    t += r

print(t)
