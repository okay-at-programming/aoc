from collections import deque

rules = {}

for l in open('data'):
    if not l:
        continue
    elif '=>' in l:
        a,b = [c.strip() for c in l.split('=>')]

        if a not in rules:
            rules[a] = []

        rules[a].append(b)
    else:
        string = l.strip()

print(rules)


seen = set()
q = deque()
q.append(('e',0))
t = 1

while len(q) > 0:
    s, steps = q.popleft()

    if s == string:
        print(steps)
        break
    if s in seen:
        continue
    if len(s) > len(string):
        continue

    seen.add(s)

    if steps > t:
        print(t, len(q), len(s), len(string))
        t += 1

    for k in rules.keys():
        r = s.find(k)
        while r >= 0:
            for rep in rules[k]:
                ns = s[:r] + rep + s[r+len(k):]
                q.append((ns,steps+1))
            r = s.find(k, r+1)

