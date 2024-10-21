data = open('data').read().strip()

f = 0
p = 1

for c in data:
    if c == '(':
        f += 1
    elif c == ')':
        f -= 1
    else:
        assert False

    if f == -1:
        print(p)
    p += 1

print(f)

