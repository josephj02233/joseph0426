import random
xando = []

for i in range(0,4):
   xando.append([])
   for j in range(0,4):
      switch = random.randint(0,1)
      if switch == 1:
         xando[i] += "x"
      else:
         xando[i] += "o"
for values in xando:
   output=""
   for value in values:
      output+=value
   print(output)
