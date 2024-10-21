m = {'A A': 4, 'A B': 8, 'A C': 3, 'B A': 1, 'B B': 5, 'B C': 9, 'C A': 7, 'C B': 2, 'C C': 6}

x = {'A': 'C', 'B': 'A', 'C': 'B'}
z = {'A': 'B', 'B': 'C', 'C': 'A'}

t = 0
for l in open('data'):
    i,j = l.strip().split()

    if j == 'X':
        t += m[i + ' ' + x[i]]
    elif j == 'Y':
        t += m[i +  ' ' + i]
    elif j == 'Z':
        t += m[i + ' ' + z[i]]

print(t)
