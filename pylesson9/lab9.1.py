num = [2,6,8,9,10,12,13,15,17,24,55,66,78,77,79]

def gfactor():
    for i in range(2,num):
        if num % i == 0:
            return 1
        else:
            return 0

def removeprime():
    for i in num:
        if gfactor==0:
          num.remove(i)
print(removeprime())
print(num)
