# Andre Mendoza
# 3/4/25
# P1HW2
# Create a program to budget traveling expenses

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

print('---------------Travel Expenses---------- ')
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"Fuel: ${gas_cost:.2f}")
print(f"Accommodation: ${accommodation_cost:.2f}")
print(f"Food: ${food_cost:.2f}")
print(f"Remaining Balance: ${remaining_balance:.2f}")


