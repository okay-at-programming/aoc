data = [x.strip() for x in open('data')]

g = ''
e = ''
for i in range(len(data[0])):
    x = 0
    y = 0

    for l in data:
        if l[i] == '0':
            x += 1
        if l[i] == '1':
            y += 1

    #g *= 2
    #e *= 2
    if x > y:
        g += '1'
        e += '0'
    elif True: #> x:
        e += '1'
        g += '0'

print(e,g)

e = int(e,2)
g = int(g,2)
print(g,e,g*e)
