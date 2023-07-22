print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill? $ '))
percentage_tip = int(
    input('What percentage tip would you like to give? 10, 12, or 15? '))
number_people = int(input('How many people to split the bill? '))
person = (total_bill * (1 + percentage_tip / 100)) / number_people

print(f'Each person should pay: ${"{:.2f}".format(person)}')
