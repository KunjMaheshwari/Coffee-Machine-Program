from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_onn = True

while is_onn:
    options = menu.get_items()
    choice = input(f"What would you like to drink? ({options})")
    if choice == "off":
        is_onn = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        print = coffee_maker.is_resource_sufficient(drink)
        if print == True:
            payment = money_machine.make_payment(drink.cost)
            if payment == True:
                coffee_maker.make_coffee(drink)
