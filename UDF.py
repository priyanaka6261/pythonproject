def maxoftwo(a,b):
    if a>b:
        print("a is greator")
    else:
        print("b is greator")
def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print("a is greator")
        else:
            print("c is greator")
    elif b>c:
            print("b is greator")
    else:
        print("c is greator")
def febonacci(n):
    a,b =0,1
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
    print()
def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
                print("not prime")
                break
        else:
            print("prime")
            
    
        
        
        
