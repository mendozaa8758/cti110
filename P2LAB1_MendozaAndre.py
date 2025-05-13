# Andre Mendoza
# 3/9/25
# P2LAB1
# Use tools to create formulas to find the diameter, circumference, and area of a circle
import math

# Plug in the radius
radius = float(input('What is the radius of the circle?'))

# Calculate the diameter

diameter = 2 * radius

# Calculate the circumference
circumference = 2 * math.pi * radius

# Calculate the area
area = math.pi * (radius ** 2)

# Display the diameter, circumference, and area of the circle
print(f"The diameter of the circle is: {diameter:.1f}")
print(f"The circumference of the circle is: {circumference:.2f}")
print(f"The area of the circle is: {area:.3f}")
