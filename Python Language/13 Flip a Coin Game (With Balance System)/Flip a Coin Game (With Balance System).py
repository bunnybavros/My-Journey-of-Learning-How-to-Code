import random
import time

#Ask user to start the game.
Start = str(input("Would you like to start the game? (y/n): "))

while True:
    if Start == "n" or Start == "N":
        print("Nevermind, you can come back later if you want to!")
        exit()
    elif Start == "y" or Start == "Y":
        print("Welcome to the Head and Tail Game!")
        time.sleep(1)
        print("To play this game is really simple, you will need to guess the coin if it was head or tail.")
        print("1 Guessing cost 20$ and if you won the game, you'll get 38$!")
        print("Enjoy!!\n\n\n")
        print("Head = 1 and Tail = 2")
        
        #Default Setting
        Balance = 200
        Result = None
        Guess = None
        
        while True:
            #Game System
            HeadTail = random.randint(1,2)
            Win = 38
            Play = 20
            #print(HeadTail) #Enable this for cheat mode.

            #Condition variables
            if HeadTail == 1:
                Result = 1
            else:
                Result = 2
                
            #The main game (Ask user to guess and balance system)
            print("\n\nYour balance is", Balance, "$")
            Guess = int(input("Head or Tail? (1/2): "))
            if Guess == 1 or Guess == 2:
                if Balance >= 20:
                    Balance = Balance - Play
                    print("Your balance is now", Balance, "$")
                    if int(Guess) == Result: #Check if player win or lost
                        time.sleep(1)
                        print("\n\nCorrect, you have won", Win, "$ from the game!")
                        Balance = Balance + Win
                        print("Your balance is now", Balance, "$")
                        print("\n_______________________")
                        time.sleep(1)
                    else:
                        time.sleep(1)
                        print("\n\nSorry, you lost.")
                        print("\n_______________________")
                        time.sleep(1)
                else:
                    print("\n\n_______________________")
                    print("\n\n\nSorry, you don't have enough balance to play the game.")
                    restart = str(input("Press enter to restart the game.\n\n"))
                    break
    else:
        print("\nPlease only enter -y-, -Y-, -n- or -N- to continue.")
        break
