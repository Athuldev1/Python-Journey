# Define constants for the machine resources and values
resources = {"water": 200, "milk": 150, "coffee": 100, "money": 0}

drink_requirements = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18},
    "latte": {"water": 200, "milk": 150, "coffee": 24},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24},
}

drink_costs = {
    "espresso": 1.5,
    "latte": 2.5,
    "cappuccino": 3.0,
}

COINS_AND_VALUES = {"QUARTER": 0.25, "DIME": 0.10, "NICKEL": 0.05, "PENNY": 0.01}


def report():
    """Display the available resources on the machine."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def check_resources(drink):
    """Check if there are enough resources to make the selected drink."""
    missing_resources = []
    for item in drink_requirements[drink]:
        if resources[item] < drink_requirements[drink][item]:
            missing_resources.append(item)
    if missing_resources:
        print(f"Sorry, there is not enough: {', '.join(missing_resources)}.")
        return False
    return True


def calculate_coin_value(quarter, dime, nickel, penny):
    """Calculate the total value of inserted coins."""
    total_value = (
        quarter * COINS_AND_VALUES["QUARTER"]
        + dime * COINS_AND_VALUES["DIME"]
        + nickel * COINS_AND_VALUES["NICKEL"]
        + penny * COINS_AND_VALUES["PENNY"]
    )
    return total_value


def get_coin_input():
    """Get the number of each type of coin from the user."""
    try:
        quarter = int(input("How many Quarters? "))
        dime = int(input("How many Dimes? "))
        nickel = int(input("How many Nickels? "))
        penny = int(input("How many Pennies? "))
        return quarter, dime, nickel, penny
    except ValueError:
        print("Invalid input! Please enter a valid number of coins.")
        return 0, 0, 0, 0


is_machine_on = True
while is_machine_on:
    selected_drink = input(
        "What would you like? (espresso/latte/cappuccino/report): "
    ).lower()

    if selected_drink == "report":
        report()
    elif selected_drink == "off":
        print("Machine is closing...")
        is_machine_on = False
    elif selected_drink in ["espresso", "latte", "cappuccino"]:
        if check_resources(selected_drink):
            print("Please insert the coins.")
            quarter, dime, nickel, penny = get_coin_input()

            total = calculate_coin_value(quarter, dime, nickel, penny)
            print(f"The total value of coins inserted is ${total:.2f}.")

            drink_cost = drink_costs[selected_drink]
            if total > drink_cost:
                change = total - drink_cost
                print(f"Here is your {selected_drink}. Your change is ${change:.2f}.")

                # Deduct the resources used to make the drink
                for item in drink_requirements[selected_drink]:
                    resources[item] -= drink_requirements[selected_drink][item]

                # Add money to the machine
                resources["money"] += drink_cost
            elif total == drink_cost:
                print(f"Here is your {selected_drink}. Thank you for the exact amount.")
                for item in drink_requirements[selected_drink]:
                    resources[item] -= drink_requirements[selected_drink][item]
                resources["money"] += drink_cost
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            print(
                f"{selected_drink.capitalize()} cannot be made due to insufficient resources."
            )
    else:
        print("Wrong input! Please select any of the available drinks.")
