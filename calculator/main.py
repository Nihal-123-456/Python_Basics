from math_functions import *
from ui_functions import user_choice_input

while True:
    print(user_choice_input())
    again = input('Do you want to perform another operation? (y/n): ')
    if again.lower() != 'y':
        break