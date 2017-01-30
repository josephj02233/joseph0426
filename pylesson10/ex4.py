import random

numlist=[]
for i in range(0,4):
   numlist.append([])
   for j in range(0,4):
      numlist[i].append(random.randint(1,100))

for nums in numlist:
   output=""
   for num in nums:
      output += str(num)+" "
   print(output)


div=int(input("Please enter a num:"))
count=0
for nums in numlist:
   for num in nums:
      if num%div == 0:
        count+=1
print("There are",count,"numbers divisible by",div,"in the list.")
