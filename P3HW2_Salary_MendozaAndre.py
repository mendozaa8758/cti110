# Andre Mendoza
# 3/31/25
# P3HW2
# Create a salary calculator that includes overtime, gross pay, and net pay

# Get employee details

name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked this week: "))
pay_rate = float(input("Enter employee's pay rate: "))
# Find out overtime and overtime rate
overtime= 40
overtime_rate = 1.5
# Find regular and overtime pay
if hours_worked > overtime:
    overtime_hours = hours_worked - overtime
    regular_hours = overtime
else:
        overtime = 0
        regular_hours = hours_worked
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * overtime)
gross_pay = regular_pay + overtime_pay
# Show off the salary
print('------------------------------------------')
print(f'Employee name: {name}')
print(' ')
print(f"{'Hours Worked':<20} {'Pay Rate':<20} {'Overtime Hours':<20} {'Overtime Pay':<20} {'Regular Pay':<20} {'Gross Pay':}")
print('----------------------------------------------------------------------------------------------------------------------------------------------')
print(f"{hours_worked:<20} {pay_rate:<20} {overtime_hours:<20} ${overtime_pay:<20.2f}     ${regular_pay:<10.2f}     ${gross_pay:<20.2f}")
