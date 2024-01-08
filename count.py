file=open("second.txt","w")
file.write("hey friends how are\ni hope you all are good\nso we are here to complete handling the file")
file.close()
file=open("second.txt","r")
c=file.read()
print(c)
number_of_lines=0
number_of_words=0
number_of_chars=0
for line in c:
    number_of_lines+=1
    line=line.strip("\n")
    list1=line.split()
    number_of_words+=len(list1)
    number_of_chars+=len(line)
file.close()
print("the number of lines=",number_of_lines)
print("the number of words=",number_of_words)
print("the number of chars=",number_of_chars)



