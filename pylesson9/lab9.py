mylist = ["joseph","ben","hanna","nicole","lala"]

print("In order...")
output=""
for i in mylist:
    output+=i+" "
print(output)
print(" ")
print("Reversed...")

def reverse(mylist):
    j=""
    for i in range(len(mylist)-1,-1,-1):
        j+=mylist[i]+" "
        print(j)
        

reverse(mylist)
    
