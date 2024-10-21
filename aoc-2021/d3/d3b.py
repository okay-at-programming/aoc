data = [x.strip() for x in open('data')]

o = [x for x in data]
c = [x for x in data]
for i in range(len(data[0])):
    x = 0
    y = 0

    if len(o) > 1:
        for l in o:
            if l[i] == '0':
                x += 1
            if l[i] == '1':
                y += 1

        if x > y:
            o = [x for x in o if x[i] == '0']
        else:
            o = [x for x in o if x[i] == '1']

    x = 0
    y = 0

    if len(c) > 1:
        for l in c:
            if l[i] == '0':
                x += 1
            if l[i] == '1':
                y += 1

        if x <= y:
            c = [x for x in c if x[i] == '0']
        else:
            c = [x for x in c if x[i] == '1']


o = int(o[0],2)
c = int(c[0],2)
print(o,c,o*c)
