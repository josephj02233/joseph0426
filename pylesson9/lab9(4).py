start=int(input("please enter your staring nums:"))
size=int(input("please enter your sequence size:"))
seq=[]
for i in range(0,size):
    if i == 0 or i ==1 :
        seq.append(start)
    else:
        seq.append(seq[i-1]+seq[i-2])
print(seq)
