mprog = [int(i) for i in open('data', 'r').read().strip().split(',')]

class computer:
  def __init__(self, program):
    self.program = [i for i in program]
    self.i = 0
    self.base = 0

  def comp(self, input1, input2):
    cont = True
    output = None
    while cont:
      rule = self.program[self.i]
      opcode = rule%100

      if opcode == 99:
        cont = False
        break

      mode = int(rule/100)
      c = mode%10
      mode = int(mode/10)
      b = mode%10
      mode = int(mode/10)
      a = mode%10

      res = 0
      if opcode == 1:
        val1 = self.val(self.i+1, c)
        val2 = self.val(self.i+2, b)
        val3 = self.val(self.i+3, a)

        res = self.prog(val1) + self.prog(val2)
        self.set(val3, res)
        self.i += 4
      elif opcode == 2:
        val1 = self.val(self.i+1, c)
        val2 = self.val(self.i+2, b)
        val3 = self.val(self.i+3, a)

        res = self.prog(val1) * self.prog(val2)
        self.set(val3, res)
        self.i += 4
      elif opcode == 3:
        val1 = self.val(self.i+1, c)
        res = input2 if input1 is None else input1
        input1 = None
        self.set(val1, res)
        self.i += 2
      elif opcode == 4:
        val1 = self.val(self.i+1, c)
        output = self.prog(val1)
        self.i += 2
        return None, output
      elif opcode == 5:
        val1 = self.val(self.i+1, c)
        val2 = self.val(self.i+2, b)

        if self.prog(val1):
          self.i = self.prog(val2)
        else:
          self.i += 3
      elif opcode == 6:
        val1 = self.val(self.i+1, c)
        val2 = self.val(self.i+2, b)

        if not self.prog(val1):
          self.i = self.prog(val2)
        else:
          self.i += 3
      elif opcode == 7:
        val1 = self.val(self.i+1, c)
        val2 = self.val(self.i+2, b)
        val3 = self.val(self.i+3, a)

        self.set(val3, 1 if self.prog(val1) < self.prog(val2) else 0)
        self.i += 4
      elif opcode == 8:
        val1 = self.val(self.i+1, c)
        val2 = self.val(self.i+2, b)
        val3 = self.val(self.i+3, a)

        self.set(val3, 1 if self.prog(val1) == self.prog(val2) else 0)
        self.i += 4
      elif opcode == 9:
        val1 = self.val(self.i+1, c)

        self.base += self.prog(val1)
        self.i += 2

    return output, None

  def val(self, j, a):
    val = j if a == 1 else self.prog(j)
    if a == 2:
      val += self.base
    return val

  def prog(self, j):
    if j < 0:
      print('error')
    while len(self.program) <= j:
      self.program.append(0)
    return self.program[j]

  def set(self, j, k):
    if j < 0:
      print('error')
    while len(self.program) <= j:
      self.program.append(0)
    self.program[j] = k

def check(x,y):
  return computer(mprog).comp(x,y)[1]

for y in range(10):
  row = ''
  for x in range(10):
    row += str(check(x,y))
  print(row)

t = 99
x = 3
y = 4
while True:
  if check(x,y-t) and check(x+t,y-t):
    print(x,y-t)
    print(10000*x + y-t)
    break

  x += 1
  while check(x,y+1):
    y += 1
