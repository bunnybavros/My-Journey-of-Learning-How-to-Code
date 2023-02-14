#Make a multiplication table from User's input.

#Input
Number = input("What is the number that you would liked to make the multipliication table?: ")

#Compare the input of the user
#If number is a digit, then make a multiplication table
#But if it not a digit, then give user an error message.
if Number.isdigit():
    for Multiplication in range(1, 13):
            print(Multiplication, "*", Number, "=", Multiplication * int(Number))
else:
    print("ERROR 01: Please enter a number.")
