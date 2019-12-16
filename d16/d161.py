signal = open('data.txt','r').read().strip()

pattern = 0,1,0,-1

def pat(i,j):
  return pattern[((j+1)//(i+1))%4]

for j in range(100):
  newsig = ''
  for p in range(len(signal)):
    r = 0
    for i,s in enumerate(signal):
      a = int(s)
      o = a*pat(p,i)
      r += o
    newsig += str(r)[-1]
  print(newsig)
  signal = newsig

print(' ', signal[:8])