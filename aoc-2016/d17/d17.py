from collections import deque
from hashlib import md5

vault = (3,3)

base = 'pvhmgsws'

p = (0,0)
q = deque()
q.append((p,''))

while q:
    p, path = q.popleft()

    if p == vault:
        print(path)
        break

    h = md5((base+path).encode()).hexdigest()

    if p[1] > 0 and h[0] in 'bcdef':
        np = p[0], p[1]-1
        q.append((np,path + 'U'))


    if p[1] < 3 and h[1] in 'bcdef':
        np = p[0], p[1]+1
        q.append((np,path + 'D'))

    if p[0] > 0 and h[2] in 'bcdef':
        np = p[0]-1, p[1]
        q.append((np,path + 'L'))

    if p[0] < 3 and h[3] in 'bcdef':
        np = p[0]+1, p[1]
        q.append((np,path + 'R'))

