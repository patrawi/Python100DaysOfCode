import random

player_choice = int(input(
    'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n'))

bot_choice = random.randint(0, 2)
if player_choice == 0:
    print('You chose: Rock')
    if bot_choice == 0:
        print('Computer chose: Rock')
        print('You draw \n-')
    elif bot_choice == 1:
        print('Computer chose: Paper')
        print('You lose \n-')
    elif bot_choice == 2:
        print('Computer chose: Scissors')
        print('You win \n-')
elif player_choice == 1:
    print('You chose: Paper')
    if bot_choice == 0:
        print('Computer chose: Rock')
        print('You win \n-')
    elif bot_choice == 1:
        print('Computer chose: Paper')
        print('You draw \n-')
    elif bot_choice == 2:
        print('Computer chose: Scissors')
        print('You lose \n-')
elif player_choice == 2:
    print('You chose: Scissors')
    if bot_choice == 0:
        print('Computer chose: Rock')
        print('You lose \n-')
    elif bot_choice == 1:
        print('Computer chose: Paper')
        print('You win \n-')
    elif bot_choice == 2:
        print('Computer chose: Scissors')
        print('You draw \n-')
else:
    print('You chose wrong move')
    exit()
