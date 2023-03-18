rno=int(input("enter roll no"))
name=input("enter your name")
s1=int(input("enter marks of subject :1"))
s2=int(input("enter marks of subject:2"))
total=s1+s2
per=total/3
print("roll no",rno)
print("studentname",name)
print("total",total)
print("%",per)
if per>70:
    print("distinctiion")
elif per>60:
    print("first division")    
elif per>=50:
    print("second divisiom")
else:
    print("fail")        
