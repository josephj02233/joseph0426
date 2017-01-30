class car:
    def __init__(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    def setcustom(self, newp, newi, newe, newt):
        self.paint = newp
        self.interior = newi
        self.engine = newe
        self.tires = newt

    def getpaint(self):
        return self.paint
    def getinterior(self):
        return self.interior
    def getengine(self):
        return self.engine
    def gettires(self):
        return self.tires
    
        
def main():
    p=input("please enter the number of the paint: ")
    i=input("please enter the number of the interior: ")
    e=input("please enter the number of the engine: ")
    t=input("please enter the number of the tires: ")

    user1=car( p, i, e, t)
    
    print("Paint: ", user1.getpaint())
    
    print("Interior: ", user1.getinterior())
    print("Engine: ", user1.getengine())
    print("Tires: ", user1.gettires())


main()


    
        

    
