data = open('data', 'r').read().strip()

aord = ord('a')

shortest = len(data)

for shift in range(26):
    cata = ''
    lower = chr(aord + shift)
    upper = lower.upper()

    for char in data:
        if char != lower and char != upper:
            cata += char

    i = 0

    while i < len(cata)-1:
        curr = None
        if cata[i].isupper():
            curr = cata[i].lower()
        else:
            curr = cata[i].upper()

        if curr == cata[i+1]:
            cata = cata[:i] + cata[i+2:]
            if i > 0:
                i -= 2
            else:
                i -= 1

        i += 1

    if len(cata) < shortest:
        shortest = len(cata)

print(shortest)
