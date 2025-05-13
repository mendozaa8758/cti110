# Andre Mendoza
# 3/16/25
# P2HW1
# THis assignment is remaking P1HW2 to have nicer formatting.

# Ask for the budget
budget =float(input("Enter budget: "))

# Enter their destination
destination = input("Enter your travel destination: ")

# Enter how much they'll spend on gas
gas_cost = float(input("Enter how much you'll spend on gas: "))

# Enter how much they'll spend on accommodation
accommodation_cost = float(input("Enter how much you'll spend on accomodation: "))

# Enter how much they will spend on food
food_cost = float(input("Enter how much you'll spend on food: "))

# Find the total expense
total_expense = food_cost + gas_cost + accommodation_cost

# Calculate remaining balance
remaining_balance = budget - total_expense

# Display initial budget, destination, expenses breakdown, total expenses, and remaining balance
print('------------Travel Expenses------------')
print("{:<20} {:>10}".format("Location:", destination))
print("{:<20} ${:>10.2f}".format("Initial Budget:", budget))
print("{:<20} ${:>10.2f}".format("Fuel:", gas_cost))
print("{:<20} ${:>10.2f}".format("Accommodation:", accommodation_cost))
print("{:<20} ${:>10.2f}".format("Food:", food_cost))
print("{:<20} ${:>10.2f}".format("Total Expenses:", total_expense))
print('---------------------------------------')
print("{:<20} ${:>10.2f}".format("Remaining Balance:", remaining_balance))
