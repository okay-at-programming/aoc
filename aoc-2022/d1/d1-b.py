lines = open('data').read()

e = lines.split('\n\n')

d = [f.strip().split('\n') for f in e]

g = sorted([sum([int(h) for h in j]) for j in d])

print(sum(g[-3:]))
