from math_functions import *

def user_choice_input():
    user_choice = input(''' 
    Welcome to the calculator app
    1. For addition press 1
    2. For subtraction press 2
    3. For multiplication press 3
    4. For division press 4
    '''
    )
    output = user_choice_action(user_choice)
    return output

def user_choice_action(user_choice):
    if user_choice == '1':
        nums = input('''
        Please enter the numbers you want to add
        Make sure they are separated by space
        ''')
        return add(nums)

    elif user_choice == '2':
        num1 = int(input('''
        Please enter the numbers you want to subtract
        First enter the minuend :               
        '''))
        num2 = int(input('Now enter the subtraend : '))
        return subtract(num1, num2)

    elif user_choice == '3':
        nums = input('''
        Please enter the numbers you want to multiply
        Make sure they are separated by space
        ''')
        return multiply(nums)

    elif user_choice == '4':
        num1 = int(input('''
        Please enter the numbers you want to divide
        First enter the dividend :               
        '''))
        num2 = int(input('Now enter the divisor : '))
        return divide(num1, num2)

    else:
        return 'Invalid input'