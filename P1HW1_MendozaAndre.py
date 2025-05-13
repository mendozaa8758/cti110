# Andre Mendoza
# 3/3/25
# P1HW1
# Calculating Exponents and Addition and Subtraction
print('-----Calculating Exponents-----')
# Create a base and an exponent
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent value: "))
# Find the result
result = base ** exponent
# Print the result
print(f"{base} raised to the power of {exponent} is {result}!!!")

print('-----Addition and Subtraction----')

# Get three integers
num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))
# Do the calulations for each
sum_result = num1 + num2
final_result = sum_result - num3
# Show the final result
print(f"({num1} + {num2}) - {num3} is equal to {final_result}")