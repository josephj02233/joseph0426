class milesperhour:
    def __init__(self, d, h, m):
        self.distance=d
        self.hours=h
        self.minutes=m
        self.mph=0
    def setvalue(self,newdsitance,newhours,newminutes):
        self.distance=newdistance
        self.hours=newhours
        self.minutes=newminutes
        self.mph=0
        
    def getdist(self):
        return self.distance
    def gethours(self):
        return self.hours
    def getminutes(self):
        return self.minutes
    def getmph(self):
        self.mph = self.distance/(self.hours + self.minutes / 60.0)
        return self.mph

def main():
    dustance = int(input("enter the distance: "))
    hours = int(input("enter the hours: "))
    minutes = int(input("enter the minutes: "))

    newvalue=milesperhour(distance,hours,minutes)
    print(user1.getdist(),"miles in",user1.gethours(),"hours and",user1.getminutes(),"minutes ="user1.getmph(),"mph")

    newvalue.setvalue(10,2,0)
    print(user1.getdist(),"miles in",user1.gethours(),"hours and",user1.getminutes(),"minutes ="user1.getmph(),"mph")

main()
