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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

turn_off = False

def check_resources(orders_ingredients):
    '''See if ingredients are enough'''
    for item in orders_ingredients:
        if orders_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def insert_coins(cost):
    '''Check if Inserted coins are enough'''
    quartes = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money = quartes*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    if money > cost:
        return True, money-cost
    else:
        return False, money

def make_coffee(orders_ingredients):
    '''Reduce Resources'''
    global resources
    for item in orders_ingredients:
        resources[item] -= orders_ingredients[item]

while not turn_off:
    action = input("What would you like? (espressso/latte/cappuccino): ")
    if action == "report":
        print(f"Water: {resources['water']}ml\n" \
              f"Milk: {resources['milk']}ml\n" \
              f"Coffee: {resources['coffee']}g\n" \
              f"Money: ${profit}")
    elif action == "off":
        turn_off = True
    elif action == "espresso" or action == "latte" or action == "cappuccino":
        drink = MENU[action]
        if check_resources(drink["ingredients"]):
            coin_result = insert_coins(drink["cost"])
            if coin_result[0]:
                profit += drink["cost"]
                if coin_result[1] > 0:
                    print(f"Here is ${round(coin_result[1], 2)} dollars in change.")
                make_coffee(drink["ingredients"])
                print(f"Here is your {action} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Invalid Input")