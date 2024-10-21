t = 0

data = open('data').readlines()
i = 0

while i < len(data):
    a,b,c = data[i:i+3]

    i += 3

    a = set(a.strip())
    b = set(b.strip())
    c = set(c.strip())
    s = a.intersection(b).intersection(c)

    for c in s:
        if c.isupper():
            t += ord(c) - ord('A') + 27
        else:
            t += ord(c) - ord('a') + 1

print(t)

