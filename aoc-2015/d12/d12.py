d = open('data').read()

i = 0
total = 0
while i < len(d):
    j = i
    while d[j].isdigit():
        j += 1
    if d[i].isdigit():
        a = int(d[i:j])
        if i > 0 and d[i-1] == '-':
            a *= -1
        total += a
        i = j
    else:
        i += 1

print(total)
