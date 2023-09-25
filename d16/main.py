""" create coffee machine with oop"""
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    """main function"""
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    should_maintenane = False
    while not should_maintenane:
        options = menu.get_items()
        command = input(f" What would you like? ({options}) :").lower()
        if command == "off":
            should_maintenane = True
        elif command == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            item = menu.find_drink(command)
            if (
                item
                and coffee_maker.is_resource_sufficient(item)
                and money_machine.make_payment(item.cost)
            ):
                coffee_maker.make_coffee(item)


if __name__ == "__main__":
    main()
