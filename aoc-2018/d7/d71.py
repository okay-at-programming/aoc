before = {}

for line in open('data', 'r'):
    l = line.split()

    char = l[7]
    char2 = l[1]
    if char not in before:
        before[char] = set()
    if char2 not in before:
        before[char2] = set()

    before[char].add(char2)

occurred = set()
count = len(before.keys())
output = ''

while len(occurred) < count:
    possible = []

    for key, value in before.items():
        if key in occurred:
            continue

        if value <= occurred:
            possible.append(key)

    possible.sort()

    value = possible.pop(0)
    occurred.add(value)
    output += value

print(output)


