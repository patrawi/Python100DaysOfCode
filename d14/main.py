"""High Low"""
import random
from os import system
from game_data import data

GAME_LOGO = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

VS_LOGO = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def format_data(account):
    """Print a format sentence"""
    return f"{account['name']}, {account['description']}, from {account['country']}"


def compare(player_guess, a, b):
    """compare a against b"""
    if a["follower_count"] > b["follower_count"]:
        return player_guess == "a"
    return player_guess == "b"


def submit(player_answer, correct_answer):
    """check between player and solution"""
    if player_answer == correct_answer:
        return True
    return False


def choose_profile():
    """choose 1 profile from game_data"""
    random_profile = random.choice(data)

    return random_profile


def main():
    """main function"""
    player_lose = False
    player_score = 0
    a = choose_profile()
    b = choose_profile()
    print(GAME_LOGO)
    while not player_lose:
        a = b
        b = choose_profile()
        while a == b:
            b = choose_profile()
        print(f"Compare A: {format_data(a)}")
        print(VS_LOGO)
        print(f"Against B: {format_data(b)}")
        player_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        result = compare(player_answer, a, b)
        system("clear")
        print(GAME_LOGO)
        if result:
            player_score += 1
            print(f"You're right! Current score: {player_score}.")

        else:
            print(f"Sorry, that's wrong. Final score: {player_score}")
            player_lose = True


if __name__ == "__main__":
    main()
