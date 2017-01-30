import random
class user:
    def __init__(self, fname, lname, avat=""):
        self.firstname = fname
        self.lastname = lname
        self.avatar = avat
        self.userID = random.randint(0, 1000000)

    def sethes(self, newfirstname, newlastname, newavatar):
        self.firstname = newfirstname
        self.lastname = newlastname
        self.avatar = newavator
        self.userID = random.randint(0, 1000000)

    def getfirstname (self):
        return self.firstname
    def getlastname (self):
        return self.lastname
    def getavatar(self):
        return self.avatar
    def getuserID(self):
        return self.userID
    def __str__(self):
        print("Custom info...\nFirst name: ", self.firstname, "\nLast Name: ", self.lastname,"\nAvatar: ", self.avatar,"\nUser ID: ", self.userID) 
def main():
    fname = input("enter the first name:")
    lname = input("enter the last name:")
    avt = input("would tou like to use a public avatar?y or n:")
    if avt=="n":
        user1=user(fname,lname)
    else:
        avat=input("enter the avartar:")
        user1=user(fname,lname,avat)
    print(user1.__str__())
main()
        
        
    
    
        

    
