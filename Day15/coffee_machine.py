# Day 15 | Coffer Machine Program

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

QUARTER_VALUE = .25
NICKEL_VALUE = .05
DIME_VALUE = .10
PENNY_VALUE = .01

def print_report():
    """Prints out report of machine's current resources"""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]:.2f}")

def check_resources(user_order):
    """Checks if the machine has enough resources to make the requested drink"""
    item_ingredients = MENU[user_order]['ingredients']

    for key in item_ingredients:
        if item_ingredients[key] > resources[key]:
            print(f"Sorry there is not enough {key}")
            return False

    return True

def process_payment(drink):
    """Processes taking coins from the user, seeing if they have enough money for a drink,
    and gives them change if needed"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickels = int(input("how many nickels?:"))
    pennies = int(input("how many pennies?:"))

    coin_holder = [
        quarters * QUARTER_VALUE,
        dimes * DIME_VALUE,
        nickels  * NICKEL_VALUE,
        pennies * PENNY_VALUE
    ]

    user_cash = sum(coin_holder)

    if user_cash >= MENU[drink]["cost"]:
        resources["money"] += MENU[drink]["cost"]
        change = user_cash - MENU[drink]["cost"]

        print(f"Here is ${change:.2f} in change.")

        make_drink(drink)
    else:
        print("Sorry that's not enough money. Money refunded.")
        return

def make_drink(drink):
    """Removes the required resources from the machine needed to make the drink. Serves user"""
    for resource in MENU[drink]["ingredients"]:
        resources[resource] -= MENU[drink]["ingredients"][resource]

    print(f"Here is your {drink}. Enjoy!")

machine_running = True

while machine_running:
    # Prompts user for their order
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Handles internal employee codes for turning off machines and printing reports
    if order == "off":
        machine_running = False
    elif order == "report":
        print_report()
    else:
        enough_resources = check_resources(order)

        if enough_resources:
           process_payment(order)

