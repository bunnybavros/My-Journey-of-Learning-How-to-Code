#Percentage Calculator

#User Input
Price = int(input("What is the total price of items you have purchased?: "))
Percentage = int(input("How many % did they gave you for the discount?: "))

#Process of find the price after discount
Discount = (Price * Percentage) / 100
PriceAfterDiscount = Price - Discount

#Output
if PriceAfterDiscount == 0:
    print("You can take your items for free.")

elif PriceAfterDiscount >= 1:
    print("You have to pay ", PriceAfterDiscount, "$")
    
#I have learned that you need to use "==" for telling the program that if this one equals to this. not the "=" one
#Because if you are going to use "=", it would means that you are trying to create a new variable.
