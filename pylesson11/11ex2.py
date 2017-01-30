import math
class distance:
    def __init__(self, x1, y1, x2, y2):
        self.xone = x1
        self.yone = y1
        self.xtwo = x2
        self.ytwo = y2
        self.distance = 0

    def setvalue(self,newx1,newy1,newx2,newy2):
        self.xone = newx1
        self.yone = newy1
        self.xtwo = newx2
        self.ytwo = newy2
        self.distance = 0

    def getmph(self):
        self.distance= Math.sqrt((self.xtwo-self.xone)*(self.xtwo-self.xone)+(self.ytwo-self.yone)*self.ytwo-self.yone))
        return self.mph

def main():
    x1=int(input("enter a num for x1: "))
    y1=int(input("enter a num for y1: "))
    x2=int(input("enter a num for x2: "))
    y2=int(input("enter a num for y2: "))

    newuser = distance(x1, y1, x2, y2)

    print("distance = ", newuser.getmph())

main()
        
