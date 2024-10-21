data = open('data.txt', 'r').read()

layer = 25*6
layercount = int(len(data)/layer)
print(layer, layercount)

output = []

for i in range(layer):
  for j in range(layercount):
    if data[(j*layer)+i] == '0':
      output.append(' ')
      break
    elif data[(j*layer)+i] == '1':
      output.append('X')
      break

print(len(output))

for i in range(6):
  print(output[i*25:(i+1)*25])