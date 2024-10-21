datas = ['D2FE28','38006F45291200','EE00D40C823060','8A004A801A8002F478','620080001611562C8802118E34','C0015000016115A2E0802F182340','A0016C880162017C3686B18A3D4780']
data = datas[6]
data = open('data').read().strip()

def getlit(data):
    print('lit',data)
    v = int(data[:3],2)
    t = data[3:6]
    i = 6
    while data[i] == '1':
        i += 5
    return v,i+5

def getlb(data):
    print('lb',data)
    v = int(data[:3],2)
    lb = int(data[7:22],2)
    ss = data[22:22+lb]
    i = 0
    while i < lb:
        c,j = sumversion(ss)
        i += j
        ss = ss[j:]
        v += c
    return v,22+lb

def getfb(data):
    print('fb',data)
    v = int(data[:3],2)
    bc = int(data[7:18],2)
    ss = data[18:]
    i = 0
    for _ in range(bc):
       c,j = sumversion(ss)
       i += j
       ss = ss[j:]
       v += c
    return v,18+i

def sumversion(data):
    t = data[3:6]
    if t == '100':
        return getlit(data)
    else:
        lt = data[6]

        if lt == '0':
            return getlb(data)
        else:
            return getfb(data)



data = bin(int(data,16))[2:]
while len(data)%4 != 0:
    data = '0' + data

print(sumversion(data))
