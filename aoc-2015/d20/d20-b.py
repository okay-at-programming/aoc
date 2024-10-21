nums = {1:0}

t = 33100000
i = 2
while True:

    p = 11*i
    for j in range(i,i*51,i):
        nums[j] = nums.setdefault(j,0) + p

    if nums[i] >= t:
        print(i)
        break

    nums.pop(i-1)

    i += 1
