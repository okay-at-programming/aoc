d = open('data').read().strip()
#d = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

i = 4
while i < len(d):
    s = set(d[i-4:i])
    if len(s) == 4:
        print(i)
        break
    i += 1
