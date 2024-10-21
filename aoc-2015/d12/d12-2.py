data = open('data').read()

def count(i):
    red = False
    t = 0

    d = 1
    j = i + 1
    while d > 0:
        if data[j] in '{[':
            a,j = count(j)
            t += a
        elif data[j] in '}]':
            d -= 1
        elif data[j].isdigit():
            k = j
            while data[k].isdigit():
                k += 1
            a = int(data[j:k])
            if j > 0 and data[j-1] == '-':
                a *= -1
            t += a
            j = k
        elif data[j:j+6] == ':"red"':
            red = True
            j += 1
        else:
            j += 1
    if red:
        t = 0
    return t, j+1

print(count(0)[0])

