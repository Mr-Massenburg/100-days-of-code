#Day 16 | Coffee Machine with OOP. Introduction to Classes

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_running = True

while machine_running:
    order = input(f"What would you like? ({menu.get_items()}):").lower()

    if order == "off":
        machine_running = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        enough_resources = coffee_maker.is_resource_sufficient(drink)
        if enough_resources:
            valid_payment = money_machine.make_payment(drink.cost)
            if valid_payment:
                coffee_maker.make_coffee(drink)
