x = int(input("enter year"))
if((x % 400 == 0) or
     (x% 100 != 0) and
     (x% 4 == 0)):
    print("Given Year is a leap Year")
else:
    print("this is not leap year")