# case study-1 in Python for Engineers(AI102P)
x = int(input("Price of frist item : "))  # Took input for the price of the first item
y = int(
    input("Price of seccond item : ")
)  # Took input for the price of the seccond item
z = int(input("Price of third item : "))  # Took input for the price of the third item
Total = x + y + z  # Evaluated the total of all the input prices
Discounted_Price = Total * 0.10  # Evaluated the Discounted_Price with a 10% discount
if Total > 50:  # Using the if functiont to check if the total is more than $50
    print("Original Total  : ", Total)  # Printing the original Total amount
    print(
        "Discounted Amount  : ", Discounted_Price
    )  # Printing the Discounted amount if the if condition is satified
    print(
        "Final Amount : ", Total - Discounted_Price
    )  # Printing the final amount after the discountd amount is discounted from the total amount
else:  # Using the else function for the else condition when the if statement is not being applied
    print("Original Total : ", Total)  # Printing the original total amount
    print("Final Amount : ", Total)  # Printing the final amount
