file=open("text.txt","w")
file.write("hello dosto kaise hai aplog \nand one more things as you know about me i am very dedicatesd person who are very attacth to its own job of \nso lets play a game\n")
file.close()


file=open("text.txt","r")
content=file.read()       # when we use read() method then it will read entire text of file
print(content)   
file.close()


file=open("text.txt","r")
content=file.readline()   # when we use readline() method then it will show the single line before \n
print(content)
file.close()


file=open("text.txt","r")
content=file.readlines()  # when we use readlines() method then it will show the entire content of file in list format even \n will also print
print(content)
file.close()
