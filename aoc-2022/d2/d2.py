m = {'A X': 4, 'A Y': 8, 'A Z': 3, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}

t = 0
for l in open('data'):
    t += m[l.strip()]

print(t)
