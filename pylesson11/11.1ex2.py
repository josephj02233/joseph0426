class human:
    def __init__(self, h, e, s):
        self.hair = h
        self.eyes = e
        self.skin = s
    def serhes(self,nh,ne,ns):
        self.hair = nh
        self.eyes = ne
        self.skin = ns
    def geth(self):
        return self.hair
    def gete(self):
        return self.eyes
    def gets(self):
        return self.skin

def main():
    h=input("please enter the characteristic of the hairs :")
    e=input("please enter the characteristic of the eyes :")
    s=input("please enter the characteristic of the skin :")

    user1= human(h,e,s)

    print("My info....")
    print("Hair:", user1.geth())
    print("Eyes:", user1.gete())
    print("Skin:", user1.gets())

    user1.serhes("blonde","blue","white")
    print("\nFriend's info....")
    print("Hair:", user1.geth())
    print("Eyes:", user1.gete())
    print("Skin:", user1.gets())
    

main()



    
        

    
