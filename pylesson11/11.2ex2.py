import random 
class inventory:
    def __init__(self, m, n, c="", p=""):
        self.manufacture = m
        self.name = n
        self.catagory = c
        self.UPC = random.randint(0, 1000000000)
        self.price = p
    def serhes(self, newm, newn, newc):
        self.manufacture = newm
        self.name = newn
        self.catagory = newc
    def getmanufacture(self):
        return self.manufacture
    def getname(self):
        return self.name
    def getcatagory(self):
        return self.catagory
    def getUPC(self):
        return self.UPC
    def getprice(self):
        return self.price
    def __str__(self):
        print("Your item......\nManufacture: ", self.manufacture,"\nName: ", self.name,"\nCatagory: ", self.catagory,"\nUPS: ", self.UPS,"\nPrice: ", self.price)


def main():
    m=input("please enter the manufacture:")
    n=input("please enter the name:")
    yn=input("Will u be entering catogory and price info? y or n")

    if yn=='n':
        item1=inventory(m,n)
    if yn=='y':
        c=input("please enter the catagory:")
        p=int(input("please enter the price" ))
        item1=inventory(m,n,c,p)
    print(item.__str__())

main()
    
        

    
