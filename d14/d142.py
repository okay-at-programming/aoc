import math

rules = {}
for line in open('data.txt', 'r'):
  line = line.split(' => ')
  input = {}
  for i in line[0].split(', '):
    j = i.split()
    input[j[1]] = int(j[0])
  om,oc = line[1].split()
  rules[oc] = int(om),input
  
ore = 'ORE'
fuel = 'FUEL'

def getrequired(neededfuel):
  required = {i:0 for i in rules}
  have = {i:0 for i in rules}
  have[ore] =required[ore] = 0
  required[fuel] = neededfuel
  needs = neededfuel

  while needs > 0:
    for chem in required:
      if chem == ore or required[chem] == 0:
        continue
      
      nec = required[chem] - have[chem]
      if nec > 0:
        mult = math.ceil(nec/rules[chem][0])
        have[chem] += rules[chem][0] * mult
        for chem2,mult2 in rules[chem][1].items():
          required[chem2] += mult2*mult
          if chem2 != ore:
            needs += mult2*mult
      have[chem] -= required[chem]
      needs -= required[chem]
      required[chem] = 0
  return required[ore]

target = 1000000000000
unit = getrequired(1)
maxfuel = target // unit
l = maxfuel
r = maxfuel * 2
while l <= r:
  m = (l+r)//2
  if getrequired(m) > target:
    r = m - 1
  else:
    maxfuel = m
    l = m + 1

print(maxfuel)