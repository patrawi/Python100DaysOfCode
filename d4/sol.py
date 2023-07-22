import random
choices = ['Rock', 'Paper', 'Scissors']
player_choice = int(input(
    'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n'))


if player_choice > 2 or player_choice < 0:
    print('Wrong move')
else:
    player_move = choices[player_choice]
    print(f'You chose: {player_move}')
    bot_choice = random.randint(0, 2)
    print(f'Computer chose: {choices[bot_choice]}')
    if player_choice == 0 and bot_choice == 2:
        print('You win')
    elif player_choice == 2 and bot_choice == 0:
        print('You lose')
    elif player_choice > bot_choice:
        print('You win')
    elif player_choice < bot_choice:
        print('You lose')
    else:
        print('You draw')
