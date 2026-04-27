# Write a program that asks the user to enter an integer greater than 0, then
# asks whether the user wants to determine the sum or the product of all
# numbers between 1 and the entered integer, inclusive. Finally, share the
# result with them.

def calculate_sum(target):
    result = 0
    for n in range(1, target + 1):
        result += n

    return result

def calculate_product(target):
    result = 1
    for n in range(1, target + 1):
        result *= n

    return result


integer = int(input('Please enter an integer greater than 0: '))
choice = input('Enter "s" to compute the sum or "p" to compute the product. ')

if (choice == 's'):
    print(
        f'The sum of the integers between 1 and {integer} is '
        f'{calculate_sum(integer)}.'
    )
elif (choice == 'p'):
    print(
        f'The product of the integers between 1 and {integer} is '
        f'{calculate_product(integer)}.'
    )
else:
    print('Invalid selection. Please try again...')
