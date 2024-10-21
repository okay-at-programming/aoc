test = [3, 4, 1, 5]

data = [97,167,54,178,2,11,209,174,119,248,254,0,255,1,64,190]

def rev(l, s, d):
    for i in range(d//2):
        i1 = (s+i)%len(l)
        i2 = (s+d-i-1)%len(l)
        l[i1],l[i2] = l[i2],l[i1]

arr = [x for x in range(256)]
i = 0
ss = 0

for l in data:
    rev(arr,i,l)
    i = (i+l+ss)%len(arr)
    ss += 1

print(arr[0]*arr[1])
