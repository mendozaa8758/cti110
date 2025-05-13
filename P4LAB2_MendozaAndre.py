# Andre Mendoza
# 4/6/25
# P4LAB2
# Create a multiplication table for an integer between 1-12, and if it's less than zero it doesn't work.

#Define run again
run_again = 'yes'

while run_again != 'no':
    user_num = int(input('Enter an integer: '))

    if user_num >= 0:
        # Display multiplication table for 1-12
        for item in range(1, 13):
            print(f'{user_num} * {item} = {user_num * item}')
    else:
        print('This program does not handle negative values')

    run_again = input('Would you like to run the program again? (yes/no): ')

# Loop has ended
print('Exiting program...')
