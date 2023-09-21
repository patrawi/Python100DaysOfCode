"""Coffee Machine Program"""
from constant import MENU, resources, coins


def calculate():
    customer_payment = 0
    for e in coins:
        coin = int(input(f"how many {e}?: "))
        customer_payment += coin * coins[e]
    return customer_payment


def resource(command):
    for e in MENU[command]["ingredients"]:
        if MENU[command]["ingredients"][e] > resources[e]:
            print(f"Sorry there is not enough {e}")
            return False
    return True


def report(money):
    report = ""
    for r in resources:
        ingredient = r.capitalize()
        if r == "coffee":
            unit = "g"
        else:
            unit = "ml"
        report += f"{ingredient}: {resources[r]}{unit} \n"
    report += f"Money: ${money}"

    return report


def pay(customer_payment, command, money):
    change = round(customer_payment - MENU[command]["cost"], 2)
    if customer_payment >= MENU[command]["cost"]:
        for e in MENU[command]["ingredients"]:
            resources[e] -= MENU[command]["ingredients"][e]
        print(f"Here is ${change} in change.")
        print(f"Here is your {command} ☕. Enjoy!")
        money += MENU[command]["cost"]
        return money
    else:
        print("Sorry that's not enough money. Money refuneded")
        return 0


def main():
    """main function"""
    money = 0
    on_maintenance = False
    while not on_maintenance:
        command = input(" What would you like? (espresso/latte/cappuccino):").lower()
        if command == "off":
            on_maintenance = True
        elif command == "report":
            result = report(money)
            print(result)
        else:
            if command in MENU:
                if resource(command):
                    print("Please insert coins.")
                    customer_payment = calculate()
                    revenue = pay(customer_payment, command, money)
                    money += revenue


if __name__ == "__main__":
    main()
