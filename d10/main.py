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
    while True:
        
        if data['count'] == 0 :
            first_number = float(input("What's your first number?: "))
        else :
            first_number = data['result_number']
        for s in symbols:
            print(s)
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        calculate_func = symbols[operation]
        result = calculate_func(first_number, next_number)
        print(f"{first_number} {operation} {next_number} = {result}")
        decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if decision == 'y':
            data['result_number'] = result
            data['count'] += 1
        else: 
            data['result_number'] = 0
            data['count'] =0




            

if __name__ == '__main__':
    main()