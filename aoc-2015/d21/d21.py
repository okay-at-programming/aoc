weapons = []
for l in open('weapons'):
    _, c, d, a = l.split()
    weapons.append((int(c),int(d),int(a)))

armour = []
for l in open('armour'):
    _, c, d, a = l.split()
    armour.append((int(c),int(d),int(a)))

rings = []
for l in open('rings'):
    _, _, c, d, a = l.split()
    rings.append((int(c),int(d),int(a)))

def sim(player,boss):
    b = [player, boss]
    i = 0
    j = 1
    while True:
        if b[i][0] <= 0:
            return j

        d = b[i][1] - b[j][2]
        b[j][0] -= max(d, 1)

        i = (i+1)%2
        j = (j+1)%2


m = 2**10

for w in weapons:
    for a in armour:
        for r1 in rings:
            for r2 in rings:
                if r1 == r2 and r1 != (0,0,0):
                    continue

                cost = w[0] + a[0] + r1[0] + r2[0]
                dam = w[1] + a[1] + r1[1] + r2[1]
                arm = w[2] + a[2] + r1[2] + r2[2]

                if cost > m:
                    continue

                p = [100, dam, arm]
                b = [104, 8, 1]

                winner = sim(p, b)

                if winner == 0:
                    m = cost

print(m)
