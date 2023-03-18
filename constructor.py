class employee:
    def __init__(self):
        self.name='ram'
        self.salary=8999
    def getdata(self):
     print(self.name)
     print(self.salary)
e= employee()
e.getdata()
#parameterized constructo
class empl:
    def __init__(self, email,mob):
        self.email=email
        self.mob=mob
    def getdata(self):
        print(self.email)
        print(self.mob)
email= input("enter name")
mob=int(input("enter mobile"))
e1=empl(email,mob)
e1.getdata()


