file=open("first.txt","w")
file.write("hey\nhello\nfriends")
file.close()
file=open("first.txt","r")
p=file.readlines()
print(p)
file.close()
for line in p:
    print(line,end="")

