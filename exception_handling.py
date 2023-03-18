
a= int(input("enter no"))
b= int(input("enter no"))
try:
    c=a/b
    print(c)
except:
    print("denominator can never zero")
print("exit")
#print(l[5]) #it will throw an error
l=[1,2,3]
try:
    print(l[5])
except:
    print("max is three")

# file
with open("2.txt","r") as f:
    print(f.read())
try:
    #Swith open("2.txt","r") as f:
        print(f.read())
except:
    print("file not found")





