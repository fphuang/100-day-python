import menu
import supplies


def get_pay_amount(quarter, dime, nickle, penny):
    """ calculate the total amount provided the quarters, dimes, nickles and pennies"""
    return quarter * 0.25 + dime * 0.1 + nickle * 0.05 + penny * 0.01


earnings = 0

# order process
while True:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'report':
        supplies.report_supplies()
        print(f"Money: ${earnings}")
    elif choice == 'off':
        break
    else:
        result = supplies.is_supply_sufficiency(choice)
        if result is not None:
            print(f"Sorry there is not enough {result}.")
            continue
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = get_pay_amount(quarter=quarters, dime=dimes, nickle=nickles, penny=pennies)
            if not menu.check_sufficient_pay(choice, total):
                print("Sorry that's not enough money. Money refunded")
                continue
            else:
                supplies.update_supplies(choice)
                earnings += menu.get_cost(choice)
                change = total - menu.get_cost(choice)
                if change != 0:
                    print(f"Here is ${round(change, 2)} in change")
                print(f"Here is you {choice} Enjoy!")
