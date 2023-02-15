#this is so outdated but i wish this will be useful at some day... :)

#Ask user if they want to start the test.
Start = str(input("Are you ready to start the COVID-19 test? (Y/N): "))
if Start == "n" or Start == "N": #If user type n or N, then stop the test
    print("\n\nNevermind!, you can come back and start the test later...")
    exit()
elif Start == "y" or Start == "Y": #If user type y or Y, then start the test.
    print("\n\nLet's get started!")

    #Ask user 10 questions about the COVID-19 
    QuestionOne = str(input("\n\nHave you had a fever in the past few days? (Y/N): "))
    if QuestionOne == "y" or "Y" or "n" or "N":
        QuestionTwo = str(input("\n\nHave you had a persistent cough or sore throat? (Y/N): "))
        if QuestionTwo == "y" or "Y" or "n" or "N":
            QuestionThree = str(input("\n\nHave you experienced any difficulty breathing? (Y/N): "))
            if QuestionThree == "y" or "Y" or "n" or "N":
                QuestionFour = str(input("\n\nHave you been in close contact with anyone who has tested positive for COVID-19? (Y/N):"))
                if QuestionFour == "y" or "Y" or "n" or "N":
                    QuestionFive = str(input("\n\nHave you experienced any sensitivity to light or sound? (Y/N): "))
                    if QuestionFive == "y" or "Y" or "n" or "N":
                        QuestionSix = str(input("\n\nHave you recently traveled to an area with a high number of COVID-19 cases? (Y/N): "))
                        if QuestionSix == "y" or "Y" or "n" or "N":
                            QuestionSeven = str(input("\n\nHave you had any chills or shivering? (Y/N): "))
                            if QuestionSeven == "y" or "Y" or "n" or "N":
                                QuestionEight = str(input("\n\nHave you had any headaches or dizziness? (Y/N): "))
                                if QuestionEight == "y" or "Y" or "n" or "N":
                                    QuestionNine = str(input("\n\nHave you noticed any rashes or skin changes? (Y/N): "))
                                    if QuestionNine == "y" or "Y" or "n" or "N":
                                        QuestionTen = str(input("\n\nHave you experienced any chest pain or pressure? (Y/N): "))
                                        if QuestionTen == "y" or "Y" or "n" or "N":
                                            print("\n\n\n\n\nYou have done your test!")
                                        else:
                                            print("ERROR 01: Please only enter Y or N only.")
                                            exit()
                                    else:
                                        print("ERROR 01: Please only enter Y or N only.")     
                                        exit()   
                                else:
                                    print("ERROR 01: Please only enter Y or N only.")        
                                    exit()    
                            else:
                                print("ERROR 01: Please only enter Y or N only.")      
                                exit()              
                        else:
                            print("ERROR 01: Please only enter Y or N only.")  
                            exit()                  
                    else:
                        print("ERROR 01: Please only enter Y or N only.")
                        exit()
                else:
                    print("ERROR 01: Please only enter Y or N only.")
                    exit()

            else:
                print("ERROR 01: Please only enter Y or N only.")
                exit()

        else:
            print("ERROR 01: Please only enter Y or N only.")
            exit()
    else:
        print("ERROR 01: Please only enter Y or N only.")
        exit()
else:
    print("ERROR 01: Please only enter Y or N only.")
    exit()

#Score System /// Convert the answer to a integer value.
if QuestionOne == "y" or QuestionOne == "Y":
    ScoreOne = 1
else:
    ScoreOne = 0

if QuestionTwo == "y" or QuestionTwo == "Y":
    ScoreTwo = 1
else:
    ScoreTwo = 0

if QuestionThree == "y" or QuestionThree == "Y":
    ScoreThree = 1
else:
    ScoreThree = 0

if QuestionFour == "y" or QuestionFour == "Y":
    ScoreFour = 1
else:
    ScoreFour = 0

if QuestionFive == "y" or QuestionFive == "Y":
    ScoreFive = 1
else:
    ScoreFive = 0

if QuestionSix == "y" or QuestionSix == "Y":
    ScoreSix = 1
else:
    ScoreSix = 0

if QuestionSeven == "y" or QuestionSeven == "Y":
    ScoreSeven = 1
else:
    ScoreSeven = 0

if QuestionEight == "y" or QuestionEight == "Y":
    ScoreEight = 1
else:
    ScoreEight = 0

if QuestionNine == "y" or QuestionNine == "Y":
    ScoreNine = 1
else:
    ScoreNine = 0

if QuestionTen == "y" or QuestionTen == "Y":
    ScoreTen = 1
else:
    ScoreTen = 0

#Take the interger values and add them together to find the result.
Result = ScoreOne + ScoreTwo + ScoreThree + ScoreFour + ScoreFive + ScoreSix + ScoreSeven + ScoreEight + ScoreNine + ScoreTen
print("\nYour final score is:",Result, "points")

#Output the result.
if Result >= 5:
    print("According to your final score, you might have the COVID-19.")
    print("\nPlease remember that this test might not be correct.")
    print("Also try to take a chance to test with the COVID-19 tester,")
    print("and contact or talk to the doctor for more information.")

if Result <= 4:
    print("According to your final score, you might not have the COVID-19.")
    print("\nPlease remember that this test might not be correct.")
    print("Also try to take a chance to test with the COVID-19 tester,")
    print("and contact or talk to the doctor for more information.")
