#This is my first game on python ever.
#Guess the number game.

import random #Import random library

#How to play.
print("Let's play the game!")
print("To play this game, you just need to guess the random number.")
print("The system will tell you if your guess is too high or too low.")
print("Enojoy!!!")

#Generate a random number.
while True:
    RandomNumber = random.randint(1,100)
    #print(RandomNumber) #---- Enable this if you want to see what the random number is.
    Guess = None

#Make conditional for random number generation
#If user guesses the random number correctly, then they won the game.
    while RandomNumber != Guess:
        Guess = int(input("\n\nGuess the random number between (1-100): "))
        if Guess > RandomNumber: #If user guesses the random number too high, tell them.
            print("\nYour guess is too high.")
        elif Guess < RandomNumber: #If user guesses the random number too low, tell them.
            print("\nYour guess is too low.")
        else: #If user guesses the random number correctly, tell them and ask them if they want to play again.
                print("\nCorrect!")
                Again = str(input("Would you like to play this game again? (y/n): "))
    
    if Again.lower() != "y": #Check if user wants to play this game again. (!=) means not equal.
        print("\nThanks for playing!")
        exit()
    else:
        pass #pass is used when user want to make a condition by using if-else, but didn't want it to do anythong else rather than compare the value or stuff.
