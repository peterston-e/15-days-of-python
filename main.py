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

print(MENU["espresso"]["ingredients"]["water"])
print(MENU["espresso"]["cost"])

# TODO: 1 prompt user What would you like? (espresso/latte/cappuccino):
# TODO: 2 exit if the user types "off"
# TODO: 3 print report of resources and profit with "report"
# TODO: 4 check resources after being prompted for drink
# TODO: 5 process coins - "insert coins, quarters etc"
# TODO: 6 check money, if !enough, refund and exit. if ok add to profit
# TODO: 7 calculate change
# TODO: 8 make coffee - deduct resources, “Here is your latte. Enjoy!”
