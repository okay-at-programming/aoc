
def fuel(input):
  return int(input/3) - 2

def f2(input):
  total = 0
  while input >= 0:
    input = fuel(input)
    if input > 0:
      total += input
  return total
  
total = 0
for l in open('data', 'r'):
  i = int(l)
  total += f2(i)

print(total)