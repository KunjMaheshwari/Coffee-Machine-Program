# Coffee Machine using python

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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


should_continue = True


def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def coins_sufficient():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total = total + int(input("How many dimes?: ")) * 0.10
    total = total + int(input("How many nickles?: ")) * 0.05
    return total


def transacation_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print(
            f"Sorry that's not enough money. Money refunded: {money_received}.")


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


while should_continue == True:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == "off":
        should_continue = False
    elif prompt == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: ${money}")
    else:
        drink = MENU[prompt]
        if resources_sufficient(drink["ingredients"]):
            payment = coins_sufficient()
            if transacation_successful(payment, drink["cost"]):
                make_coffee(prompt, drink["ingredients"])
