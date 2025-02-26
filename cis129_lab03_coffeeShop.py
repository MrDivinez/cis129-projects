print("*****************")
print("Marco's Cafe")
# Prices of the food/drink
Smoothie_Price = 5
Bagel_Price = 2
Coffee_Price = 3
Muffin_Price = 1.50
Tax_Rate = 0.06

# Get the users input on the amount they buy
number_smoothies = int(input("enter the number of smoothies:"))
number_Bagels = int(input("enther the number of bagels:"))
number_coffees = int(input("Enter the number of coffees:"))
number_muffins = int(input("Enter the number of muffins:"))
print("*****************")
# Caculate total price
subtotal = (number_coffees * Coffee_Price) + (number_muffins * Muffin_Price) + (number_smoothies * Smoothie_Price) + (number_Bagels * Bagel_Price)

# Tax
tax = subtotal * Tax_Rate

# Caculate full total after tax
total = subtotal + tax

# Gives out the input of the users value
print("RECIEPT")
print(f"subtotal: ${subtotal:.2f}")
print(f"Tax (6%): ${tax:2f}")
print(f"total: ${total:.2f}")
print("*****************")

