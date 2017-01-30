go = input("Please enter 16 Strings:")
splist = go.split(" ")
wordlist = []

spot = 0
for i in range (0,4):
   wordlist.append([])
   for j in range (0,4):
      wordlist[i].append(splist[spot])
      spot += 1

for words in wordlist:
   output = ""
   for word in words:
      output+=word+" "
   print(output)
