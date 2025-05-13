# Andre Mendoza
# 3/16/25
# P2HW2
# Create a list showing grades, the highs and lows, and the average of said grades.

# Create an empty list to store grades
grades_list = []

# Prompt the user to enter grades for each module
grades_list.append(float(input("Enter your grade for Module 1: ")))
grades_list.append(float(input("Enter your grade for Module 2: ")))
grades_list.append(float(input("Enter your grade for Module 3: ")))
grades_list.append(float(input("Enter your grade for Module 4: ")))
grades_list.append(float(input("Enter your grade for Module 5: ")))
grades_list.append(float(input("Enter your grade for Module 6: ")))

# Calculate the required statistics
lowest_grade = min(grades_list)
highest_grade = max(grades_list)
sum_of_grades = sum(grades_list)
average_grade = sum_of_grades / len(grades_list)

#Print the lowest, highest, sum, and averages for the grades.
print('------------Results------------')
print(f"Lowest grade : {lowest_grade:>5.1f}")
print(f"Highest grade: {highest_grade:>5.1f}")
print(f"Sum of grades: {sum_of_grades:>6.1f}")
print(f"Average Grade: {average_grade:>6.2f}")
print('-------------------------------------------------')
