x= int(input("enter no for counting\n"))
sum=0
for i in range (1,2*(x+1)):
     if(i%2==0) :
        #print(i)
        sum = sum+i
print(sum)
