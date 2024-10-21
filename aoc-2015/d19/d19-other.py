import re

data = open('data').read()

molecule = data.split('\n')[-1][::-1]
reps = {m[1][::-1]: m[0][::-1]
        for m in re.findall(r'(\w+) => (\w+)', data)}
def rep(x):
    return reps[x.group()]

f = 1
count = 0
while molecule != 'e':
    molecule = re.sub('|'.join(reps.keys()), rep, molecule, 1)
    count += 1
    if count > f:
        print(count)
        f *= 2

print(count)
