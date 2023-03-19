import UDF


while True:
    print("*************")
    print("1. Maxoftwo")
    print("2. maxofthree")
    print("3.febonacci")
    print("4.prime")
    print("5. Exit")
    print("*************")


    choice=int(input("enter your choice"))
    if choice==1:
        a=int(input("enter a"))
        b=int(input("enter b"))
        UDF.maxoftwo(a,b)
        print("***************")
    elif choice==2:
        a=int(input("enter a"))
        b=int(input("enter b"))
        c=int(input("enter c"))
        UDF.maxofthree(a,b,c)
        print("***************")
    elif choice==3:    
        c=int(input("enter c"))
        UDF.febonacci(c)
        print("***************")
    elif choice==4:
        c=int(input("enter c"))
        UDF.prime(c)
        print("***************")
    else:
        print("Thankyou for our services , good bye")
        break    
    
            
 
        
    
