import time

menu = [
    {
        "Beverage": "Espresso",
        "Resources": {"water": 50, "coffee": 18, "milk": 0},
        "price": 1.50
    },
    {
        "Beverage": "Latte",
        "Resources": {"water": 200, "coffee": 24, "milk": 150},
        "price": 2.50
    },
    {
        "Beverage": "Cappuccino",
        "Resources": {"water": 250, "coffee": 24, "milk": 100},
        "price": 3.00
    }
]

current_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

coin = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

refill_resources = {
    "water": 500,
    "milk": 500,
    "coffee": 500
}


def status_report():
    print("\nCurrent resources:")
    for ingredient, volume in current_resources.items():
        print(f"{ingredient.capitalize()}: {volume}")

    print("\nAccepted coins:")
    for coin_type, value in coin.items():
        print(f"{coin_type.capitalize()}: ${value:.2f}")


def get_price(user_choice):
    for drink in menu:
        if drink["Beverage"] == user_choice:
            return drink["price"]
    return None


def cal_price(
    penny_input, nickel_input, dime_input, quarter_input, user_choice
):
    """Calculate the change due, or return None if the drink is invalid."""
    drink_price = get_price(user_choice)

    if drink_price is None:
        print("This drink has no price tag.")
        return None

    total_coins = (
        penny_input * coin["penny"]
        + nickel_input * coin["nickel"]
        + dime_input * coin["dime"]
        + quarter_input * coin["quarter"]
    )

    return round(total_coins - drink_price, 2)


def refill_machine():
    for item, amount in refill_resources.items():
        current_resources[item] += amount


def eval_price(user_choice, user_coins):
    selected_drink = None

    for drink in menu:
        if drink["Beverage"] == user_choice:
            selected_drink = drink
            break

    if selected_drink is None:
        print(f"The {user_choice} drink is not available.")
        return

    drink_price = selected_drink["price"]

    # Check resources before accepting payment.
    for ingredient, quantity in selected_drink["Resources"].items():
        if current_resources[ingredient] < quantity:
            print(f"Not enough {ingredient} to make {user_choice}.")
            print("Please refill the machine. No ingredients were used.")
            return

    # Check payment.
    if user_coins < drink_price:
        print(f"The drink costs ${drink_price:.2f}.")
        print(f"You inserted ${user_coins:.2f}.")
        print("Insufficient payment. Please collect your refund.")
        return

    # Payment is sufficient.
    change = round(user_coins - drink_price, 2)

    print(f"Payment accepted: ${user_coins:.2f}")
    print(f"The price of {selected_drink['Beverage']} is ${drink_price:.2f}.")

    if change == 0:
        print("No change is due.")
    else:
        print(f"Your change is ${change:.2f}.")

    # Deduct resources only after successful checks and payment.
    for ingredient, quantity in selected_drink["Resources"].items():
        current_resources[ingredient] -= quantity

    print(f"Here is your {selected_drink['Beverage']}. Enjoy!")


def main():
    None_refill=False
    refill_chance=2
    while True:
        print("\nThe Coffee Machine is ready.")
        print("Type 'report', 'refill', or 'off'.")

        user_choice = input(
            "Choose espresso, latte, cappuccino, report, refill, or off:\n"
        ).strip().capitalize()
        if refill_chance==0:
                print("No more refill left.")
                continue

        if user_choice == "Off":
            print("The Coffee Machine is shutting down.")
            break

        elif user_choice == "Report":
            status_report()
            continue

        elif user_choice == "Refill":
            time.sleep(3)
            refill_chance-=1
            refill_machine()
            status_report()
            print("Resources refilled.")
            continue
                
        if get_price(user_choice) is None:
            print("Sorry, that beverage is not available.")
            continue

        print("Checking current resources...")
        time.sleep(1)

        try:
            penny_input = int("".join(input("How many pennies? ")).strip())
            nickel_input = int("".join(input("How many nickels? ")).strip())
            dime_input = int("".join(input("How many dimes? ")).strip())
            quarter_input = int("".join(input("How many quarters? ")).strip())

            if min(
                penny_input,
                nickel_input,
                dime_input,
                quarter_input
            ) < 0:
                print("Coin counts cannot be negative.")
                continue

        except ValueError:
            print("Please enter whole numbers for the coin counts.")
            continue

        # Calculate the actual total payment.
        total_coins = round(
            penny_input * coin["penny"]
            + nickel_input * coin["nickel"]
            + dime_input * coin["dime"]
            + quarter_input * coin["quarter"],
            2
        )

        print("Processing transaction...")
        eval_price(user_choice, total_coins)


if __name__ == "__main__":
    main()