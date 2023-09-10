from art import logo
import random
from os import system

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

player_win = "You win 😃"
player_lose = "You lose 😤"
player_draw = "Draw 🙃"
opponent_lose = "Opponent went over. You win 😁"
opponent_win = "You went over. You lose "
opponent_blackjack = 'Lose, opponent has Blackjack 😱'
player_blackjack = 'Win with a Blackjack 😎'

def deal_card():
    """dealer give a player and computer a card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if 11 in cards and sum(cards) > 21:
        occurrence_11 = cards.count(11)
        for _ in range(occurrence_11):
            cards.remove(11)
            cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """compare the score"""
    if (
        user_score > 21
        and computer_score > 21
    ):
        return opponent_win
    if user_score == computer_score:
        return player_draw
    elif computer_score == 21:
        return opponent_blackjack
    elif user_score == 21:
        return player_blackjack
    elif user_score > 21:
        return opponent_win
    elif computer_score > 21:
        return opponent_lose
    elif computer_score < user_score:
        return player_win
    else:
        return player_lose
def main():
    """main function"""
    hands = {"player": [], "computer": []}
    print(logo)
    for _ in range(2):
        hands["player"].append(deal_card())
        hands["computer"].append(deal_card())
    should_continue = True
    while should_continue:
        player_score = calculate_score(hands['player'])
        computer_score = calculate_score(hands['computer'])
        print(
            f"\t Your cards: {hands['player']}, current score: {player_score}"
        )
        print(f"\t Computer's first card: {hands['computer'][0]}")
        if player_score > 21 or player_score == 21 or computer_score == 21:
            should_continue = False
        else:
            is_deal_another = input(
            "Type 'y' to get another card, type 'n' to pass: "
        ).lower()
            if is_deal_another == "y":
                hands["player"].append(deal_card())
            else:
                should_continue = False
    while computer_score < 17:
        hands['computer'].append(deal_card())
        computer_score = calculate_score(hands['computer'])
    print(f"Your final hand: {hands['player']}, final score: {sum(hands['player'])}")
    print(
        f"Computer's final hand: {hands['computer']}, final score: {sum(hands['computer'])}"
    )
    print(compare(player_score, computer_score))
    play_again = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': "
    ).lower()
    if play_again == "y":
        system("clear")
        main()
    else:
        exit()


if __name__ == "__main__":
    decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if decision == "n":
        exit()
    main()
