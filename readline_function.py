f=open("story.txt","r")
data=f.read(5)# read 5 character
print(data)
newdata=f.readlines()# read all lines from file and display in form of list
print(newdata)
f.close()
