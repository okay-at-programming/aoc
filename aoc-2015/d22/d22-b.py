from collections import deque

php = 50
pm = 500
bhp = 55
bd = 8

q = deque()
q.append((php,pm,0,0,0,bhp,bd,0,0))

mm = 2**20

f = 1

while q:
    php, pm, se, pe, re, bhp, bd, sm, t = q.popleft()

    if t%2 == 0:
        php -= 1

    if php <= 0:
        continue

    if pe > 0:
        bhp -= 3

    if bhp <= 0:
        if sm < mm:
            print('sol:',sm)
            mm = sm
        continue

    if re > 0:
        pm += 101

    if t%2 == 1:
        d = max(bd - (7 if se > 0 else 0), 1)
        php -= d
        q.append((php,pm, max(se-1,0), max(pe-1,0), max(re-1,0), bhp, bd, sm, t+1))
        continue

    # mm
    if pm >= 53:
        q.append((php, pm-53, max(se-1,0), max(pe-1,0), max(re-1,0), bhp-4, bd, sm+53, t+1))

    # d
    if pm >= 73:
        q.append((php+2, pm-73, max(se-1,0), max(pe-1,0), max(re-1,0), bhp-2, bd, sm+73, t+1))

    # s
    if pm >= 113 and se <= 1:
        q.append((php, pm-113, 6, max(pe-1,0), max(re-1,0), bhp, bd, sm+113, t+1))

    # p
    if pm >= 173 and pe <= 1:
        q.append((php, pm-173, max(se-1,0), 6, max(re-1,0), bhp, bd, sm+173, t+1))

    # r
    if pm >= 229 and re <= 1:
        q.append((php, pm-229, max(se-1,0), max(pe-1,0), 5, bhp, bd, sm+229, t+1))

    if len(q) > f:
        print(len(q))
        f *= 10

print('min:', mm)
