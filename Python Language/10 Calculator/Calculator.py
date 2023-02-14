#THE HARDEST ONE AT THIS MOMENT... CALCULATOR.........

#Ask user for the first number.
FirstNumber = float(input("Please enter your first number: "))

#Ask user for the second number
SecondNumber = float(input("\nPlease enter your second number: "))

#Ask user what did they want to do with these numbers.
print("\nWhat do you this number to do with the second number? Pick One.")
print("\nOption 1: Summation (+)")
print("Option 2: Subtraction (-)")
print("Option 3: Multiplication (*)")
print("Option 4: Division (/)")
print("\nONLY USE NUMBER TO PICK THE OPTION... \n(ETC. IF YOU WANT TO SUMMATION, TYPE 1)")
Choice = int(input("\nPick a number (1-4): "))

#Calculate the numbers by using the choice that user selected.
if Choice == 1:
    Answer = FirstNumber + SecondNumber
elif Choice == 2:
    Answer = FirstNumber - SecondNumber
elif Choice == 3:
    Answer = FirstNumber * SecondNumber
else:
    Answer = FirstNumber / SecondNumber

#Output the answer
print("\n\n\nThe answer is", Answer, ".")
