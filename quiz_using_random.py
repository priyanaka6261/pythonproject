import random

def choose():
    words=['cat','bat','mango','guvava']
    word=random.choice(words)
    return word
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def thanks(p1,pp1):
    print(f'{p1} your final score is {pp1}')
    print("thanks for playing")

def play():
    pp1=0
    pp2=0
    turn=0
    p1= input(" enter player 1 name")
    p2= input(" enter player 2 name ")
    while(1):
        picked_word = choose()
        qn = jumble(picked_word)
        print(qn)
        ans= input("enter your answer")
        if(ans==picked_word):
            pp1+=1
            print(f'{p1} your score is{pp1}')
        else:
            print("better luck next time i selected:" ,picked_word)
            c= int(input("enter 1 for continue 0 for quit"))
            if(c==0):
                thanks(p1,pp1)
                break
play()
