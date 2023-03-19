import random
num=random.randint(1,20)
while True:
    guess=int(input("gues no between 1  to 20"))
    if guess==num:
        print("you guessed correct number")
        break
    elif guess<num:
        print("higher number please")
    elif guess>num:
        print("lower no please")
        
              
                    
