r,c = 1,1

code = 20151125

while True:
    if r == 2978 and c == 3083:
        print(r,c,code)
        break
    code = (code*252533)%33554393
    if r == 1:
        r = c+1
        c = 1
    else:
        r -= 1
        c += 1

