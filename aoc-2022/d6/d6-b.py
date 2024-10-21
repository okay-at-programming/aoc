d = open('data').read().strip()
#d = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

i = 14
while i < len(d):
    s = set(d[i-14:i])
    if len(s) == 14:
        print(i)
        break
    i += 1
