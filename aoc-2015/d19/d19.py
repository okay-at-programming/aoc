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

out = set()
for i in range(len(string)):

    if string[i] in rules:
        for rep in rules[string[i]]:
            ns = string[:i] + rep + string[i+1:]
            out.add(ns)
    if i+1 < len(string) and string[i:i+2] in rules:
        for rep in rules[string[i:i+2]]:
            ns = string[:i] + rep + string[i+2:]
            out.add(ns)

print(len(out))

