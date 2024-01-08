f1=open("second.txt","r")
f2=open("third.txt","w")
print(f1.read())
for line in f1:
    print(f2.write(line))
f1.close()
f2.close()    