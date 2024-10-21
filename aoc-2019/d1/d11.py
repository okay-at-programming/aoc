
def fuel(input):
  return int(input/3) - 2
  
total = 0
for l in open('data', 'r'):
  i = int(l)
  total += fuel(i)

print(total)