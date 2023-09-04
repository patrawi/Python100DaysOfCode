'''blind auction'''
from os import system
from art import logo


def find_highest(bidding_record):
    '''find the highest bidding'''
    _max = 0
    winner = ''
    for bidder in bidding_record :
        if bidding_record[bidder] > _max:
            _max = bidding_record[bidder]
            winner = bidder
    return winner, _max
       

def main():
    """main function"""
    bidder = {}
    end_auction = False
    print(logo)
    print('Welcome to the secret auction program.')
    while not end_auction:
        name = input('What is your name?: ')
        bid = int(input("What's your bid?: $"))
        bidder[name] = bid
        should_continue = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
        if should_continue == 'no':
            end_auction = True
        elif should_continue == 'yes':
            system('clear')
        else:
            print('Wrong input')
            exit()
    winner, bid = find_highest(bidder)
    print(f"The winner is {winner} with a bid of ${bid}")
        


if __name__ == "__main__":
    main()
