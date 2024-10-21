data = open('data', 'r').read().strip()

i = 0

while i < len(data)-1:
    curr = None
    if data[i].isupper():
       curr = data[i].lower()
    else:
       curr = data[i].upper()

    if curr == data[i+1]:
        data = data[:i] + data[i+2:]
        if i > 0:
            i -= 2
        else:
            i -= 1

    i += 1

print(data)
print(len(data))
