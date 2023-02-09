'''Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. 
   This is how it should work when run in a terminal:
    Hello! What is your name?
    KBTU

    Well, KBTU, I am thinking of a number between 1 and 20.
    Take a guess.
    12

    Your guess is too low.
    Take a guess.
    16

    Your guess is too low.
    Take a guess.
    19
'''
import random
def guess():
    print("Hello! What is your name?")

    a = str(input())

    print("Well", a, "I am thinking of a number between 1 and 20.")
    c = (random.randint(1,20))
    print(c) #for check
    print("Take a guess.")

    b = int(input())

    if b!=c:
        print("Your guess is too low./nTake a guess.")
        b = int(input())
        if b!=c:
            print("Your guess is too low./nTake a guess.")
            b = int(input())
            if b==c:
                print("Good job,",a,"!You guessed my number in 3 guesses!")
            else:
                print("Fail")    
        else:
            print("Good job,",a,"! You guessed my number in 2 guesses!")   
    else:
        print("Good job,",a,"! You guessed my number in 1 guess!")
        
guess()