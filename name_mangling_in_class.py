class employee:
    def __init__(self,name,id):
        self.__name=name
        self.__id=id
    def getdata(self):
        print(self.__name)
        print(self.__id)
e=employee("nisha",123)
e.getdata()
e.__name="naman"
print(e.__name)#name mangling
print(dir(e))#dirfunction
e.getdata()
#print(e.__id)
