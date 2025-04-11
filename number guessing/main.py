import random
from game_functions import check_guess

number = random.randint(1, 100)
right_guess = False
guesses = 0

for i in range(0,7):
    try:
        guess = int(input(f'Guess {i+1}/7. Enter a number:'))
    except ValueError:
        print('Invalid input. Enter an integer.')
        continue
    
    guesses += 1
    result = check_guess(number, guess)

    if result == 'correct':
        right_guess=True
        break
    elif result == 'invalid':
        print("Invalid guess. You can guess between 1 and 100.")
    else:
        print(f'Your guess is {result}')

if right_guess == False:
    print(f'Sorry! you lost. The correct number was {number}.')    
else:
    print(f'Congratulations! You have won. It took you {guesses} guesses.')