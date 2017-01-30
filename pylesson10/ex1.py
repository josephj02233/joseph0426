import random
numlist=[]

for i in range(0,4):
   numlist.append([])
   for j in range(0,4):
      numlist[i].append(random.randint(1,100))

for nums in numlist:
   output=""
   for num in nums:
      output+=str(num)+" "
   print(output)
