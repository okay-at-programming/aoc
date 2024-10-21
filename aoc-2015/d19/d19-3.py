from collections import deque

rules = {}

for l in open('data'):
    if not l:
        continue
    elif '=>' in l:
        a,b = [c.strip() for c in l.split('=>')]

        if b not in rules:
            rules[b] = []

        rules[b].append(a)
    else:
        string = l.strip()

print(rules)


seen = set()
q = deque()
q.append((string ,0))
t = 1

while len(q) > 0:
    s, steps = q.popleft()

    if s == 'e':
        print(steps)
        break
    if s in seen:
        continue

    seen.add(s)

    if steps > t:
        print(steps, len(q), len(s), len(string))
        t += 1

    for k in rules.keys():
        i = s.find(k)
        while i >= 0:
            for rep in rules[k]:
                ns = s[:i] + rep + s[i+len(k):]
                q.append((ns,steps+1))
            i = s.find(k,i+1)
