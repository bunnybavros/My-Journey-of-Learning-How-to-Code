#THE HARDEST ONE AT THIS MOMENT... CALCULATOR.........

while True:
    try: #Ask user for the first number.
        FirstNumber = float(input("Please enter your first number: "))
    except ValueError:
        print("ERROR 01: Please only enter the number.\n\n")
        continue
    else: #Ask user for the second number
        try: #Ask user for the second number.
            SecondNumber = float(input("\nPlease enter your second number: "))
        except ValueError:
            print("ERROR 01: Please only enter the number.\n\n")
            continue
        else:
            #Ask user what did they want to do with these numbers.
            print("\nWhat do you this number to do with the second number? Pick One.")
            print("\nOption 1: Summation (+)")
            print("Option 2: Subtraction (-)")
            print("Option 3: Multiplication (*)")
            print("Option 4: Division (/)")
            print("\nONLY USE NUMBER TO PICK THE OPTION... \n(ETC. IF YOU WANT TO SUMMATION, TYPE 1)")
            try:
                Choice = int(input("\nPick a number (1-4): "))
            except ValueError:
                print("ERROR 01: Please only enter the number.\n\n")
                continue
            else: #Calculate the numbers by using the choice that user selected.
                if Choice == 1:
                    Answer = FirstNumber + SecondNumber
                    print("You have selected to SUMMATION\n")
                elif Choice == 2:
                    Answer = FirstNumber - SecondNumber
                    print("You have selected to SUBTRACTION\n")
                elif Choice == 3:
                    Answer = FirstNumber * SecondNumber
                    print("You have selected to MULTIPLICATION\n")
                else:
                    Answer = FirstNumber / SecondNumber
                    print("You have selected to DIVISION\n")

        #Output the answer
        print("\n\nThe answer is", Answer, ".\n\n")
    break
