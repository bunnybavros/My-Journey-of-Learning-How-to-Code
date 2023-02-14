#This program will check if the number that user put in is a positive number or a nagative number.

#User's Input
try:
    Number = float(input("Enter a number to check it out: "))

#Error Message
except ValueError:
    print("ERROR 01: Please only enter a number.")

#If not error, then do this and output the result
else:
    if Number > 0:
        print("This number is positive.")
    elif Number < 0:
        print("This number is negative.")
    else:
        print("This number is zero.")

#I finally learned how to use TRY/EXCEPT/ELSE! :))))
#This is so much easy to make an error message while the code still work normally.
