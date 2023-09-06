from art import logo
import math
from os import system
def add(f_num,n_num):
    '''addition'''
    return f_num + n_num

def substaction(f_num, n_num):
    '''substraction'''
    return f_num - n_num

def multiplication(f_num, n_num):
    '''multiply 2 numbers'''
    return f_num * n_num

def divination(f_num, n_num):
    '''divide 2 numbers'''
    if n_num == 0:
        return math.nan
    return f_num / n_num
def main():
    '''main function'''
    print(logo)
    symbols = {
        '+' : add,
        '-': substaction,
        '*' : multiplication,
        '/': divination
    }
    data = {
        'result_number' :0,
        'count' : 0
    }
    should_continue = True
    first_number = float(input("What's your first number?: "))
    for s in symbols:
            print(s)
    while should_continue:
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        calculate_func = symbols[operation]
        result = calculate_func(first_number, next_number)
        print(f"{first_number} {operation} {next_number} = {result}")
        decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if decision == 'y':
            first_number = result
        else: 
            should_continue = False
            system('clear')
            main()




            

if __name__ == '__main__':
    main()