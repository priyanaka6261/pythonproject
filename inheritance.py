class student:
    def __init__(self,name,enroll,branch):
        self.name=name
        self.enroll=enroll
        self.branch=branch
    def getinfo(self):
        print(self.name)
        print(self.enroll)
        print(self.branch)
class MST(student):
    def __init__(self,name,enroll,branch):
        super().__init__(name, enroll, branch)
    def set_mst_marks(self,python,java):
        self.python=python
        self.java=java
class EST(student):
    def set_est_marks(self,python1,java1):
        self.python1=python1
        self.java1=java1

class result(MST,EST):
    def finalresult(self):
        self.finalpython=self.python+self.python1
        self.finaljava=self.java+self.java1
        super().getinfo()
        print("total marks of python",self.finalpython)
        print("total marks of java",self.finaljava)
r1=result((input("enter name")),int(input("enter roll")),input("enter branch"))
r1.set_mst_marks(23,21)
r1.set_est_marks(67,64)
r1.finalresult()


