# Andre Mendoza
# 3/9/25
# P2LAB2
# Create a dictionary that shows the Miles per gallon for a set of cars.

# Creating the dictionary
car_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Store all the keys into a variable
car_keys = car_mpg.keys()

# Print the variable that holds the keys
print("Car models:", list(car_keys))

# Ask to enter a vehicle to see it's miles per gallon
selected_car = input("Enter a vehicle to see its mpg: ")

# Display the MPG for the chosen car
selected_car in car_mpg
print(f"The {selected_car} has {car_mpg[selected_car]} MPG.")

# Ask how long you will drive the selected car
miles = float(input(f"How many miles will you drive the {selected_car}? "))

 # Calculate the gallons of gas needed
gallons_needed = miles / car_mpg[selected_car]

# Display the amount of gas needed to drive the car
print(f"You will need {gallons_needed:.2f} gallons of gas to drive {miles} miles in a {selected_car}.")
