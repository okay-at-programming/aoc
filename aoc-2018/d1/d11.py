f = open('input', 'r')

total = 0

for line in f:
    delta = int(line[1:])
    if line[0] == "+":
        total += delta
    else:
        total -= delta

print(total)

