import menu

SUPPLIES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report_supplies():
    print(f"Water: {SUPPLIES['water']}ml")
    print(f"Milk: {SUPPLIES['milk']}ml")
    print(f"Coffee: {SUPPLIES['coffee']}g")


def update_supplies(coffee):
    ingredients = menu.get_ingredients(coffee)
    for key in ingredients:
        SUPPLIES[key] -= ingredients[key]


def is_supply_sufficiency(coffee):
    """ check if the supply is enough for the coffee """
    ingredients = menu.get_ingredients(coffee)
    for key in ingredients:
        if SUPPLIES[key] < ingredients[key]:
            return key

    return None
