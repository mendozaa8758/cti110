# Andre Mendoza
# 4/20/25
# P5LAB
# Using user-defined funtions

import random

def disperse_change(change):
    
    # Convert amount to cents
    cents = round(change * 100)

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

def main():
    # Logic goes here

    # Generate the amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    # Create variable for money put into the machine
    money_in = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change owed
    change = money_in - amount_owed
    print(f"Change owed: ${change:.2f}")

    # Call disperse change function
    disperse_change(change)

# Call the main function
main()
