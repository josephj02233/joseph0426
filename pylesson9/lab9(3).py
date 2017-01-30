number=[]
import random

for i in range(0,10):
    number.append(random.randint(1,100))

print("Numbers...")

output=""
for i in number:
    output+=str(i)+" "

print(output)

print()

def average(nums):
    sum=0
    for i in nums:
        sum += 1
    return sum/len(nums)

print("The average of the above num is", average(number))
