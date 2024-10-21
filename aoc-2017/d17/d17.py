loop = {0:0}

c = 0

for i in range(1,2018):
    for _ in range(349):
        c = loop[c]

    loop[i] = loop[c]
    loop[c] = i
    c = i

print(loop[2017])
