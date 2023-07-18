print(''' 
  __ ___   _____ _ __   __ _  ___ 
 / _` \ \ / / _ \ '_ \ / _` |/ _ \
| (_| |\ V /  __/ | | | (_| |  __/
 \__,_| \_/ \___|_| |_|\__, |\___|
                        __/ |     
                       |___/    
''')
print('Welcome to Treasure Island. \nYour mission is to find the treasure.')
first_decision = input(
    "You're at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()
if first_decision == 'left':
    second_decision = input(
        "You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if second_decision == 'wait':
        third_decision = input(
            'You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n').lower()
        if third_decision == 'yellow':
            print('You found the treasure! You Win!')
        else:
            print('You fell into a hole. Game Over')
    else:
        print('You fell into a hole. Game Over')
else:
    print('You fell into a hole. Game Over')
