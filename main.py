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
        return True


# print(MENU["espresso"]["ingredients"]["water"])
# print(MENU["espresso"]["cost"])

# prompt user for drink.
choice = input("What would you like? (espresso/latte/cappuccino): ")

# check resources after being prompted for drink
item = check_resources(choice)
if item != True:
    print(f"Sorry there is not enough {item}.")

# process coins - "insert coins, quarters etc"
print("Please insert coins")
total_dollars = 0
for coin in currency:
    num_coin = int(input(f"how many {coin}: "))
    total_dollars += num_coin * currency[coin]

# print(f"test - {'{0:.2f}'.format(total_dollars)}")

# TODO: 6. check money, if !enough, refund and exit. if ok add to profit
profit += total_dollars
# TODO: 7. calculate change
# TODO: 8. make coffee - deduct resources, “Here is your latte. Enjoy!”
# TODO: 2. exit if the user types "off"
# TODO: 3. print report of resources and profit with "report"
