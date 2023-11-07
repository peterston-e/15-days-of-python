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
}

currency = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

profit = 0


def check_resources(drink):
    water = MENU[drink]["ingredients"]["water"]
    coffee = MENU[drink]["ingredients"]["coffee"]
    if drink != "espresso":
        milk = MENU[drink]["ingredients"]["coffee"]
    else:
        milk = 0

    if water > resources["water"]:
        return "water"
    elif coffee > resources["coffee"]:
        return "coffee"
    elif milk > resources["milk"]:
        return "milk"
    else:
        return "enough"


# print(MENU["espresso"]["ingredients"]["water"])
# print(MENU["espresso"]["cost"])
make_coffee = True
while make_coffee == True:
    # prompt user for drink.
    choice = input(" What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}ml")
        print(f"Money: ${'{0:.2f}'.format(profit)}")
    elif choice == "off":
        make_coffee = False
    else:
        # check resources after being prompted for drink
        item = check_resources(choice)
        if item != "enough":
            print(f"Sorry there is not enough {item}.")

        # process coins - "insert coins, quarters etc"
        print("Please insert coins")
        total_dollars = 0
        for coin in currency:
            num_coin = int(input(f"how many {coin}: "))
            total_dollars += num_coin * currency[coin]

    # print(f"test - {'{0:.2f}'.format(profit)}") ## .format() returns a string though

    # TODO: 6. check money, if !enough, refund and exit. if ok add to profit
        price_of_drink = MENU[choice]["cost"]
        if total_dollars < price_of_drink:
            print("Sorry that's not enough money. Money refunded.")
        else:
            profit += price_of_drink
            change = total_dollars - price_of_drink
            print(f"Here is ${change} in change.")
            print(f"Here is your {choice} ☕ . Enjoy!")
            resources["water"] -= MENU[choice]["ingredients"]["water"]
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            if choice != "espresso":
                resources["milk"] -= MENU[choice]["ingredients"]["milk"]


