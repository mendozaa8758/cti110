# Andre Mendoza
# 3/23/25
# P3LAB
# Create a program that displays a float as coins and dollars.

# Get user input
amount = float(input("Enter a money amount: "))

# Convert amount to cents
cents = int(amount * 100)

# If no money is entered, print "No change"
if cents == 0:
    print("No change")
else:
    # Define the coin values
    dollar = 100
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1
    
    # Count each type of coin using // and subtraction
    dollars = cents // dollar
    cents -= dollars * dollar
    
    quarters = cents // quarter
    cents -= quarters * quarter
    
    dimes = cents // dime
    cents -= dimes * dime
    
    nickels = cents // nickel
    cents -= nickels * nickel
    
    pennies = cents // penny
    cents -= pennies * penny
    
    # Print the results
    if dollars > 0:
        print(dollars, "Dollar" if dollars == 1 else "Dollars")
    if quarters > 0:
        print(quarters, "Quarter" if quarters == 1 else "Quarters")
    if dimes > 0:
        print(dimes, "Dime" if dimes == 1 else "Dimes")
    if nickels > 0:
        print(nickels, "Nickel" if nickels == 1 else "Nickels")
    if pennies > 0:
        print(pennies, "Penny" if pennies == 1 else "Pennies")

