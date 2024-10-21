
def get(line):
    s = line.index('[') + 1
    e = line.index(']')
    return [int(x) for x in line[s:e].split(', ')]

def comp(i, a, b, c, reg):
    r = [x for x in reg]
    if i == 0:
        r[c] = r[a] + r[b]
    elif i == 1:
        r[c] = r[a] + b
    elif i == 2:
        r[c] = r[a] * r[b]
    elif i == 3:
        r[c] = r[a] * b
    elif i == 4:
        r[c] = r[a] & r[b]
    elif i == 5:
        r[c] = r[a] & b
    elif i == 6:
        r[c] = r[a] | r[b]
    elif i == 7:
        r[c] = r[a] | b
    elif i == 8:
        r[c] = r[a]
    elif i == 9:
        r[c] = a
    elif i == 10:
        r[c] = 1 if a > r[b] else 0
    elif i == 11:
        r[c] = 1 if r[a] > b else 0
    elif i == 12:
        r[c] = 1 if r[a] > r[b] else 0
    elif i == 13:
        r[c] = 1 if r[a] == r[b] else 0
    elif i == 14:
        r[c] = 1 if r[a] == b else 0
    elif i == 15:
        r[c] = 1 if a == r[b] else 0
    else:
        print('error')
    return r

t = 0
start = None
expected = None
data = None
cont = True
for line in open('data.txt'):
    if line.strip():
        cont = True
    elif not cont:
        break
    else:
        cont = False

    if line.startswith('Before'):
        start = get(line)
    elif line.startswith('After'):
        expected = get(line)
        c = 0
        for i in range(16):
            o = comp(i, data[1], data[2], data[3], start)
            if o == expected:
                c += 1
        if c >= 3:
            t += 1
    elif line[0].isdigit():
        data = [int(x) for x in line.split(' ')]

print(t)

