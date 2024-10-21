test = 'AoC 2017'

data = '97,167,54,178,2,11,209,174,119,248,254,0,255,1,64,190'
#data = test

def rev(l, s, d):
    for i in range(d//2):
        i1 = (s+i)%len(l)
        i2 = (s+d-i-1)%len(l)
        l[i1],l[i2] = l[i2],l[i1]

def dh(l):
    a = l[0]
    for b in l[1:]:
        a = a^b
    return a

data = [ord(c) for c in data]
data.extend([17, 31, 73, 47, 23])

arr = [x for x in range(256)]
i = 0
ss = 0

for _ in range(64):
    for l in data:
        rev(arr,i,l)
        i = (i+l+ss)%len(arr)
        ss += 1

denseh = [dh(arr[j:j+16]) for j in range(0,256,16)]

output = ''

for c in denseh:
    output += hex(c)[2:]

print(output, len(output))
