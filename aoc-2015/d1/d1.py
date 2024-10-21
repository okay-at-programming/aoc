data = open('data').read().strip()

f = 0

for c in data:
    if c == '(':
        f += 1
    elif c == ')':
        f -= 1

print(f)

