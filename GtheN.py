print("welcome to 'Guess the Number'")
print("Insruction")
print("1)The computer will think of a number")
print("2)you need to guess the number and type it in the given space")
print("Let's Begin")
print("I am thinking of a number........")
print("(Hint:the number is between 1-100)")
import random
snumber=random.randint(1,100)
guess=0
attempt=0
score=0
while guess!=snumber:
    try:
        guess=int(input("Make a Guess--"))
        attempt+=1
        if guess>snumber:
            print("Hmmm, too big to be true")
        elif guess<snumber:
            print("hmmm, too small to be true")
        else:
            print("Congratulations, you got it right!!!")
    except ValueError: print("Please enter a valid number!(p.s enter a number)") 
        
    
    
        
        
