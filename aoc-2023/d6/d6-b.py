time = (71530,)
distance= (940200,)
time = (42899189,)
distance=  (308117012911467,)

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

