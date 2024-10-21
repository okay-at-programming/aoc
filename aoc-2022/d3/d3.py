t = 0
for line in open('data'):
    line = line.strip()
    l = len(line)//2
    a = line[:l]
    b = line[l:]

    a = set(a)
    b = set(b)
    s = a.intersection(b)

    for c in s:
        if c.isupper():
            t += ord(c) - ord('A') + 27
        else:
            t += ord(c) - ord('a') + 1

print(t)

