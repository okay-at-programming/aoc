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
required = {i:0 for i in rules}
have = {i:0 for i in rules}
required[ore] = have[ore] = 0
required[fuel] = 1
needs = 1

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

print(required)
print(have)