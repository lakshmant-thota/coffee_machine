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


# TODO : 2.check if resources are sufficient
def is_resources_sufficient(order_ingredients):
    """checks if the resources available are sufficient for the drink choosen."""
    for ingredient in order_ingredients:
        if resources[ingredient] < order_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


# TODO : 3. process coins
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


# TODO 4. create a function to check if transaction is successful
def is_transaction_successful(money_deposited, cost):
    global profit
    if money_deposited < cost:
        print("Sorry that's not enough money.Money refunded.")
        return False
    else:
        profit += cost
        change = money_deposited - cost
        print(f"Here is ${round(change, 2)} dollars in change.")
        return True


# TODO 5. Make coffee
def make_coffee(drink_name, coffe_ingredients):
    """deducts the ingredients from the resources"""
    for item in coffe_ingredients:
        resources[item] -= coffe_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy")


should_continue = True
while should_continue:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        should_continue = False
        break
    elif choice == 'report':
        # TODO : 1. print report of all coffe machine resources
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(drink_name=choice, coffe_ingredients=drink["ingredients"])
