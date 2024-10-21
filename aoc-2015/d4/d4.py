import hashlib

sk = 'ckczppom'
i = 1

while True:
    v = sk + str(i)
    o = hashlib.md5(v.encode()).hexdigest()
    if o.startswith('00000'):
        print(i)
        break
    i += 1
