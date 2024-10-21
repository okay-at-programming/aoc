m = {'(':')','{':'}','[':']','<':'>'}
score = {')': 1,']': 2,'}': 3,'>': 4}
scores = []
for l in open('data'):
    s = []
    i = 0
    l = l.strip()
    ok = True
    while i < len(l):
        c = l[i]
        if c in ('(','[','{','<'):
            s.append(c)
        else:
            if len(s) == 0 or c != m[s[-1]]:
                ok = False
                break
            s.pop(-1)
        i += 1

    if ok:
        v = 0
        for c in ''.join(reversed([m[x] for x in s])):
            v *= 5
            v += score[c]
        scores.append(v)

scores.sort()
i = (len(scores))//2
print(scores[i])


