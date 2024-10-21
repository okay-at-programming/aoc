time = (7, 15,  30)
distance= (9, 40, 200)
time = (42,    89,    91,    89)
distance=  (308,  1170  ,1291  ,1467)

ans = 1
for i in range(len(time)):
    t = time[i]
    d = distance[i]

    total = 0
    ct = 0
    while ct <= t:
        tl = t-ct
        dt = tl*ct

        if dt > d:
            total += 1

        ct += 1

    print(total)
    ans *= total

print(ans)

