from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coin = MoneyMachine()
machine = CoffeeMaker()
menu = Menu()
turn_off = False

while not turn_off:
    coffee = input(f"What would you like? {menu.get_items()}: ")
    if coffee == "off":
        turn_off = True
    elif coffee == "report":
        machine.report()
        coin.report()
    elif coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        asked_coffee = menu.find_drink(coffee)
        if machine.is_resource_sufficient(asked_coffee) and coin.make_payment(
            asked_coffee.cost
        ):
            machine.make_coffee(asked_coffee)
    else:
        print("Invalid Imput")
