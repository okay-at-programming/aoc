t = 3310000

def prop_facts(n):
    if n%2 ==1:
        return 0
    r = 1
    i = 2
    while n > 1:
        if n%i == 0:
            j = 1
            k = 1
            while n%i == 0:
                n /= i
                j *= i
                k += j
            r *= k
        i += 1
    return r


i = 0
while True:
    i += 1

    p = prop_facts(i)

    if p >= t:
        print('answer', i)
        break
    if i %10000 == 0:
        print(i, p)
