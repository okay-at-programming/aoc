m = {'(':')','{':'}','[':']','<':'>'}
score = {')': 3,']': 57,'}': 1197,'>': 25137}

t = 0
for l in open('data'):
    s = []
    i = 0
    l = l.strip()
    while i < len(l):
        c = l[i]
        if c in ('(','[','{','<'):
            s.append(c)
        else:
            if len(s) == 0 or c != m[s[-1]]:
                t += score[c]
                break
            s.pop(-1)
        i += 1

print(t)

