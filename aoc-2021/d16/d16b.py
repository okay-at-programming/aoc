datas = ['C200B40A82','04005AC33890','880086C3E88112','CE00C43D881120','D8005AC2A8F0','F600BC2D8F','9C005AC2F8F0','9C0141080250320F1802104A08']
data = datas[1]
data = open('data').read().strip()

def getvalue(t,vs):
    v = 0
    if t == 0:
        v = sum(vs)
    elif t == 1:
        v = 1
        for a in vs:
            v *= a
    elif t == 2:
        v = min(vs)
    elif t == 3:
        v = max(vs)
    elif t == 5:
        v = 1 if vs[0] > vs[1] else 0
    elif t == 6:
        v = 1 if vs[0] < vs[1] else 0
    elif t == 7:
        v = 1 if vs[0] == vs[1] else 0

    return v

def getlit(data):
    v = int(data[:3],2)
    t = int(data[3:6],2)
    i = 6
    s = ''
    while data[i] == '1':
        s += data[i+1:i+5]
        i += 5
    s += data[i+1:i+5]
    s = int(s,2)
    return s,i+5

def getlb(data):
    v = int(data[:3],2)
    lb = int(data[7:7+15],2)
    t = int(data[3:6],2)
    ss = data[22:22+lb]
    i = 0
    vs = []
    while i < lb:
        c,j = sumversion(ss)
        i += j
        ss = ss[j:]
        vs.append(c)

    v = getvalue(t,vs)

    return v,22+lb

def getfb(data):
    v = int(data[:3],2)
    t = int(data[3:6],2)
    bc = int(data[7:18],2)
    ss = data[18:]
    i = 0
    vs = []
    for _ in range(bc):
       c,j = sumversion(ss)
       i += j
       ss = ss[j:]
       vs.append(c)

    v = getvalue(t,vs)

    return v,18+i

def sumversion(data):
    t = data[3:6]
    if t == '100':
        return getlit(data)
    else:
        lt = data[6]

        if lt == '0':
            return getlb(data)
        elif lt == '1':
            return getfb(data)
        else:
            assert False


bc = len(data)*4
data = bin(int(data,16))[2:].zfill(bc)

print(sumversion(data))
