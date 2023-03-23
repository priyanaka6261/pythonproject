d1={'a':100,'b':200,'c':300}
d2={'a':400,'b':200,'d':400}
d3=d2
for key,value in d1.items():
    if key in d2:
        d3[key]=value+d2[key]
    else:
        d3[key]=value
print(d3)        
