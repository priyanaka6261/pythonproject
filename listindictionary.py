list1=['a','b','c','d','e']
list2=[1,2,3,4,5]
dict={}
for key in list1:
    for value in list2:
        dict[key]=value
        list2.remove(value)
        break
print(dict)    
