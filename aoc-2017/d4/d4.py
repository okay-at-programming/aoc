c = 0

for line in open('data'):
    words = set()
    words.update(line.split())
    if len(words) == len(line.split()):
        c += 1

print(c)
