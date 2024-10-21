

def valid(val):
  sval = str(val)
  prev = '0'
  doub = False
  for i in range(6):
    if not doub and sval[i] == prev and (i < 2 or sval[i] != sval[i-2]) and (i == 5 or sval[i] != sval[i+1]):
      doub = True
    if sval[i] < prev:
      return False
    prev, pp = sval[i], prev
  return doub

count = 0

print(valid(112233))
print(valid(123444))
print(valid(111122))

for i in range(359282,820401):
  if valid(i):
    count += 1
print(count)