data = [int(x) for x in open('data').read().split()]

banks = [ 0, 2, 7, 0]
banks = data

seen = set()

while True:
    m = 0
    mi = -1
    for i,b in enumerate(banks):
        if b > m:
            m = b
            mi = i

    i = mi

    rem = banks[i]
    banks[i] = 0
    i = (i+1)%len(banks)
    while rem > 0:
        banks[i] += 1
        rem -= 1
        i = (i+1)%len(banks)

    state = tuple(banks)
    print(state)
    if state in seen:
        break
    seen.add(state)

print(len(seen)+1)

