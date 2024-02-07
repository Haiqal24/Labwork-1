
"""
    Program Purpose: To ask user to input data and calculate the surface area based on the given formula
    and types of shapes (cube, sphere & cylinder).
    Programmer: Haiqal
    Date: 2 February 2024
"""


print("Welcome to the Currency Converter!")

print()

print("Exchange Rate : ")
print("Exchange Rate USD : 0.21 ")
print("Exchange Rate EUR : 0.19 ")
print("Exchange Rate SGD : 0.28 ")

print()
# Prompt the user to choose the type of the currency
print("Select your target currency:")
print("1. USD - US Dollar")
print("2. EUR - Euro")
print("3. SGD - Singapore")

# Declaration of a constant
USD = 4.77
EUR = 5.13
SGD = 3.55
print()
choice = int(input("Enter your choice (1 or 2 or 3): "))

if choice == 1:
    total_amount = float(input("Enter your ammount in MYR :"))
    total = total_amount/USD
    print("Total convert is : ", total )

elif choice == 2:
    total_amount = float(input("Enter your ammount in MYR:"))
    total = total_amount/EUR
    print("Total convert is : ", total )

elif choice == 3:
    total_amount = float(input("Enter your ammount in MYR:"))
    total = total_amount/SGD
    print("Total convert is : ", total )

else:
    print('Invalid option! Please enter number 1 or 2 or 3.')



