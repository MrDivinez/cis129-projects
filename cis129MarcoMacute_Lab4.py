# Lab 4 Part 1

# Variables 
myAge = 32
yourAge = 18
myNumber = 81
yourNumber = 17
votingAge = 18
# compares your age with mine and checks if your age is less than mine and if its more then it won't qualify
if myAge == 32 and yourAge < myAge:
    print("My age is 31 and your age is less than that")
else:
    print("Our ages do not qualify")
# Lets you know if my age is between the ranges of 32 and 35 and if its not then it won't be within the range and prints the next statement
if myAge <= 35 and myAge >= 32:
    print("My age is between 32 and 35")
else:
    print("My age is not within that range")
# It grabs your age and sees if your age qualifies for the votingAge and lets you know if you can vote or not
if yourAge == votingAge or yourAge > votingAge:
    print("You can vote")
else:
    print("You cannot vote")
# Takes my number and your number and sees if it equals the same amount
if myNumber == 83 or yourNumber == 83:
    print("One of our numbers is 83")
else:
    print("83 is not our number")

# These are seperated from two different parts of the lab

# Module 4 part 4
# Marco Macute
#  3/4/25
# The program caculates the monthly sales and sales increase and within given value, the more sales the more bonus the employee gets

# The main function
def main():
    # declare local variables
    monthlySales = 0  # monthly sales amount
    storeAmount = 0   # store bonus amount
    empAmount = 0     # employee bonus amount
    salesIncrease = 0  # percent of sales increase

    # call to getSales()
    monthlySales = getSales("Enter the monthly sales amount: ")

    # call to getIncrease()
    salesIncrease = getIncrease("Enter the percent increase in sales: ")

    # call to calcStoreBonus()
    storeAmount = calcStoreBonus(monthlySales)

    # call to calcEmpBonus()
    empAmount = calcEmpBonus(salesIncrease)

    # call to printBonus()
    printBonus(storeAmount, empAmount)

# This function gets the monthly sales
def getSales(prompt):
    monthlySales = float(input(prompt))
    return monthlySales

# This function gets the percent of increase in sales
def getIncrease(prompt):
    salesIncrease = float(input(prompt))
    salesIncrease = salesIncrease / 100  # Convert percentage to decimal
    return salesIncrease

# This function determines the store bonus amount from each monthly sale
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        return 6000
    elif monthlySales >= 100000:
        return 5000
    elif monthlySales >= 90000:
        return 4000
    elif monthlySales >= 80000:
        return 3000
    else:
        return 0

# This function determines the employee bonus amount from certain sale increases
def calcEmpBonus(salesIncrease):
    if salesIncrease >= 0.05:
        empAmount = 75
    elif salesIncrease >= 0.04:
        empAmount = 50
    elif salesIncrease >= 0.03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

# This function prints the bonus information and adds an extra when reached max
def printBonus(storeAmount, empAmount):
    print(f"\nThe store bonus amount is ${storeAmount}")
    print(f"The employee bonus amount is ${empAmount}")

    if (storeAmount == 6000) and (empAmount == 75):
        print("Congrats! You have reached the highest bonus amounts possible!")

main()
