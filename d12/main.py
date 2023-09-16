"""Guessing Game"""
import random
from art import logo

levels = {"hard": 5, "easy": 10}


def get_user_guess():
    """get user guess"""
    try:
        user_guess = int(input("Make a guess: "))
        return user_guess
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_guess()


def check_guess(correct_guess, player_guess):
    """check guess"""
    if player_guess > correct_guess:
        return "Too high."
    elif player_guess < correct_guess:
        return "Too low."
    return f"You got it! The answer was {correct_guess}"


def guess(guess_try):
    """guess logic"""
    correct_guess = random.randint(1, 100)
    for i in range(guess_try):
        print(f"You have {guess_try - i} attempts remaining to guess the number.")
        user_guess = get_user_guess()
        result = check_guess(correct_guess, user_guess)
        print(result)
        if result == f"You got it! The answer was {correct_guess}":
            return
    print("You've run out of guesses, you lose.")


def main():
    """main function"""

    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level in levels:
        guess(levels[level])
    else:
        print("wrong input")
        exit()


if __name__ == "__main__":
    main()
