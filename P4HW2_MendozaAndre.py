# Andre Mendoza
# P4HW2
# 4/13/25
# Get employee details
# Create an employee salary calculator for multiple employees

# Initialize total amounts for all employees
total_regular_pay = 0
total_overtime_pay = 0
total_gross_pay = 0
total_employees = 0

# Ask for the first employee's name
name = input("Enter employee's name or type 'Done' to terminate): ")

# Loop as long as the user doesn't enter "Done"
while name.lower() != "done":
    # Get employee details
    hours_worked = float(input("Enter number of hours worked this week: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    # Overtime settings
    OVERTIME_THRESHOLD = 40
    OVERTIME_RATE = 1.5

    # find regular and overtime hours
    if hours_worked > OVERTIME_THRESHOLD:
        overtime_hours = hours_worked - OVERTIME_THRESHOLD
        regular_hours = OVERTIME_THRESHOLD
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    # Calculate pay
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * OVERTIME_RATE)
    gross_pay = regular_pay + overtime_pay

    # Print employee details
    print('------------------------------------------')
    print(f'Employee name: {name}')
    print(' ')
    print(f"{'Hours Worked':<20} {'Pay Rate':<20} {'Overtime Hours':<20} {'Overtime Pay':<20} {'Regular Pay':<20} {'Gross Pay':}")
    print('----------------------------------------------------------------------------------------------------------------------------------------')
    print(f"{hours_worked:<20} {pay_rate:<20} {overtime_hours:<20} ${overtime_pay:<20.2f} ${regular_pay:<10.2f} ${gross_pay:<20.2f}")
    
    # Add the amounts to the totals
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    total_employees += 1

    # Ask for the next employee
    name = input("Enter employee's name (or type 'Done' to finish): ")

# After the loop ends, display the total amounts
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in Gross: ${total_gross_pay:.2f}")
