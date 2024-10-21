t = 0

nums = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

def isnum(s):
    if s[0].isdigit():
        return int(s[0])

    for i,n in enumerate(nums):
        if s.startswith(n):
            return i+1

for l in open('data'):
    f = None
    e = None
    for x in range(len(l.strip())):
        d = isnum(l[x:])
        if d:
            if not f:
                f = d
            e = d
    t += 10*f + e

print(t)
