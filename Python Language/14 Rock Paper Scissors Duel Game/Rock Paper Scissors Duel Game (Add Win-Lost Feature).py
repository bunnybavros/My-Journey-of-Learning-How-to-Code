#Rock Paper Scissors Game! (complicated...) #Factorial!!!!
import random
import time

while True: #Ask if user wants to play the game.
    Start = str(input("\nWould you like to start the game? (y/n): ")).lower()
    if Start not in ["y", "n" "Y", "N"]: #Filter the wrong input out.
        print("\nPlease only enter 'y' or 'n'.")
        print("________________")
        time.sleep(0.5)
        continue
    else:
        if Start == "n":
            print("\nNevermind, you can come back again if you want to! :)")
            break
        else:
            print("\nWelcome to the Rock Paper Scissors Game!")
            print("Let's play!")
            print("________________")

            #Game Settings
            Player_Score = 0
            Bot_Score = 0
            Win = 1
            Lost = 0
            Tie = 0
            
            #Ask user what do they want to do.
            while True:
                if Player_Score == 10:
                    print("\n\n\n\n\nCongratulations!")
                    print("You won the game!")
                    print("\nYour Score:", Player_Score)
                    print("Bot Score:", Bot_Score)
                    print("\n\n\n\n\n________________\n\n\n\n\n")
                    time.sleep(2)
                    break

                if Bot_Score == 10:
                    print("\n\n\n\n\nSorry!")
                    print("Bot won the game!")
                    print("\nYour Score:", Player_Score)
                    print("Bot Score:", Bot_Score)
                    print("\n\n\n\n\n________________\n\n\n\n\n")
                    time.sleep(2)
                    break

                Bot_Choice = random.randint(1,3) #Random what bot wants to do.
                #print (Bot_Choice) #Enable this for cheat mode.
                while True:
                    print("\n1.Rock ✊")
                    print("2.Paper ✋")
                    print("3.Scissors ✌️")
                    print("4.Stop playing ❌")
                    Player_Choice = int(input("\nPick your choice: "))

                    if Player_Choice not in [1,2,3,4]: #Fliter out the wrong options.
                        print("\nPlease only enter a number between 1 and 4.")
                        print("________________")
                        time.sleep(0.5)
                        break
                    if Player_Choice == 4:
                        print("\nYou have chosen to stop playing!")
                        print("Your Score:", Player_Score)
                        print("Bot Score:", Bot_Score)
                        time.sleep(2)
                        exit()
    
                    if Player_Choice == 1 and Bot_Choice == 1:
                        print("________________")
                        time.sleep(0.5)
                        print("\nYou: Rock ✊")
                        print("Bot: Rock ✊")
                        time.sleep(0.5)
                        print("\nIt's tie!")
                        Player_Score = Player_Score + Tie #Result the User's and Bot's score.
                        Bot_Score = Bot_Score + Tie
                        print("Your Score:", Player_Score) #Display them
                        print("Bot Score:", Bot_Score)
                        print("________________")
                        time.sleep(0.5)
                        break

                    if Player_Choice == 1 and Bot_Choice == 2:
                        print("\nYou: Rock ✊")
                        print("Bot: Paper ✋")
                        time.sleep(0.5)
                        print("\nYou lost!")
                        Player_Score = Player_Score - Lost
                        Bot_Score = Bot_Score + Win
                        print("Your Score:", Player_Score)
                        print("Bot Score:", Bot_Score)
                        print("________________")
                        time.sleep(0.5)
                        break

                    if Player_Choice == 1 and Bot_Choice == 3:
                        print("\nYou: Rock ✊")
                        print("Bot: Scissors ✌️")
                        time.sleep(0.5)
                        print("\nYou won!")
                        Player_Score = Player_Score + Win
                        Bot_Score = Bot_Score + Lost
                        print("Your Score:", Player_Score)
                        print("Bot Score:", Bot_Score)
                        print("________________")
                        time.sleep(0.5)
                        break

                    if Player_Choice == 2 and Bot_Choice == 1:
                        print("\nYou: Paper ✋")
                        print("Bot: Rock ✊")
                        time.sleep(0.5)
                        print("\nYou won!")
                        Player_Score = Player_Score + Win
                        Bot_Score = Bot_Score + Lost
                        print("Your Score:", Player_Score)
                        print("Bot Score:", Bot_Score)
                        print("________________")
                        time.sleep(0.5)
                        break

                    if Player_Choice == 2 and Bot_Choice == 2:
                        print("\nYou: Paper ✋")
                        print("Bot: Paper ✋")
                        time.sleep(0.5)
                        print("\nIt's tie!")
                        Player_Score = Player_Score + Tie
                        Bot_Score = Bot_Score + Tie
                        print("Your Score:", Player_Score)
                        print("Bot Score:", Bot_Score)
                        print("________________")
                        time.sleep(0.5)
                        break

                    if Player_Choice == 2 and Bot_Choice == 3:
                        print("\nYou: Paper ✋")
                        print("Bot: Scissors ✌️")
                        time.sleep(0.5)
                        print("\nYou lost!")
                        Player_Score = Player_Score - Lost
                        Bot_Score = Bot_Score + Win
                        print("Your Score:", Player_Score)
                        print("Bot Score:", Bot_Score)
                        print("________________")
                        time.sleep(0.5)
                        break

                    if Player_Choice == 3 and Bot_Choice == 1:
                        print("\nYou: Scissors ✌️")
                        print("Bot: Rock ✊")
                        time.sleep(0.5)
                        print("\nYou lost!")
                        Player_Score = Player_Score - Lost
                        Bot_Score = Bot_Score + Win
                        print("Your Score:", Player_Score)
                        print("Bot Score:", Bot_Score)
                        print("________________")
                        time.sleep(0.5)
                        break

                    if Player_Choice == 3 and Bot_Choice == 2:
                        print("\nYou: Scissors ✌️")
                        print("Bot: Paper ✋")
                        time.sleep(0.5)
                        print("\nYou won!")
                        Player_Score = Player_Score + Win
                        Bot_Score = Bot_Score + Lost
                        print("Your Score:", Player_Score)
                        print("Bot Score:", Bot_Score)
                        print("________________")
                        time.sleep(0.5)
                        break

                    if Player_Choice == 3 and Bot_Choice == 3:
                        print("\nYou: Scissors ✌️")
                        print("Bot: Scissors ✌️")
                        time.sleep(0.5)
                        print("\nIt's tie!")
                        Player_Score = Player_Score + Tie
                        Bot_Score = Bot_Score + Tie
                        print("Your Score:", Player_Score)
                        print("Bot Score:", Bot_Score)
                        print("________________")
                        time.sleep(0.5)
                        break

                    if Player_Choice == 4:
                        print("________________")
                        print("\nThank you for playing!\n") #Thank you the user for playing
                        print("Your Score:", Player_Score) #Tell them their score again before leave.
                        print("Bot Score:", Bot_Score)
                        time.sleep(2)
                        exit()

#I just know that you can you "if" without "else".
#So I got shorter code but more function without adding else annd pass
