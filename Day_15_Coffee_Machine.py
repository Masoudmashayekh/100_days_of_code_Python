# TODO: 1. Dictionary and sources and money------------------------------------------------------------------------
Menu = {
    "espresso": {"ingredient": {"water": 50, "coffee": 18},
                 "cost": 1.5},
    "latte": {"ingredient": {"water": 200, "coffee": 24, "milk": 150},
              "cost": 2.5},
    "cappuccino": {"ingredient": {"water": 50, "coffee": 18, "milk": 100},
                   "cost": 3}
}

source = {"water": 300, "coffee": 100, "milk": 200, "money": 0}
price = {"espresso": 1.5, "latte": 2.5, "cappuccino": 3}
turn_off = False

# TODO: 2. input (What would you like? espresso/ latte/ cappuccino)-------------------------------------------------
while not turn_off:
    selection = input("What would you like? espresso/ latte/ cappuccino: ").lower()

    # TODO: 3. Report------------------------------------------------------------------------------------------------
    if selection == "report":
        for key, value in source.items():
            print(key, ":", value)

    def report():
        for key1, value2 in source.items():
            print(key1, ":", value2)

    # TODO: 4. espresso-----------------------------------------------------------------------------------------------
    if selection == "espresso" and source["water"] >= 50 and source["coffee"] >= 18:
        print("Please insert coins.")
        Quarter = int(input("How many quarters?: "))
        Dime = int(input("How many dimes?: "))
        Nickle = int(input("How many nickles?: "))
        Penny = int(input("How many pennies?: "))
        insert_coins = Quarter * 0.25 + Dime * 0.1 + Nickle * 0.05 + Penny * 0.01
        if insert_coins >= price["espresso"]:
            exchange = insert_coins - price["espresso"]
            print(f"Here is ${exchange} in change.")
            print("Here is your espresso ☕️ Enjoy!")
            source["water"] -= Menu["espresso"]["ingredient"]["water"]
            source["coffee"] -= Menu["espresso"]["ingredient"]["coffee"]
            source["money"] += Menu["espresso"]["cost"]
            [print(f"{key} : {value}") for key, value in source.items()]
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif selection == "espresso" and source["water"] < 50:
        print("Sorry there is not enough water.")
    elif selection == "espresso" and source["coffee"] < 18:
        print("Sorry there is not enough coffee.")
    else:
        # TODO: 5. latte-------------------------------------------------------------------------------------------
        if selection == "latte" and source["water"] >= 200 and source["coffee"] >= 24 and source["milk"] >= 150:
            print("Please insert coins.")
            Quarter = int(input("How many quarters?: "))
            Dime = int(input("How many dimes?: "))
            Nickle = int(input("How many nickles?: "))
            Penny = int(input("How many pennies?: "))
            insert_coins = Quarter * 0.25 + Dime * 0.1 + Nickle * 0.05 + Penny * 0.01
            if insert_coins >= price["latte"]:
                exchange = insert_coins - price["latte"]
                print(f"Here is ${exchange} in change.")
                print("Here is your latte ☕️ Enjoy!")
                source["water"] -= Menu["latte"]["ingredient"]["water"]
                source["coffee"] -= Menu["latte"]["ingredient"]["coffee"]
                source["milk"] -= Menu["latte"]["ingredient"]["milk"]
                source["money"] += Menu["latte"]["cost"]
                [print(f"{key} : {value}") for key, value in source.items()]
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif selection == "latte" and source["water"] < 200:
            print("Sorry there is not enough water.")
        elif selection == "latte" and source["coffee"] < 24:
            print("Sorry there is not enough coffee.")
        elif selection == "latte" and source["milk"] < 150:
            print("Sorry there is not enough milk.")
        else:
            # TODO: 6. cappuccino------------------------------------------------------------------------------------
            if (selection == "cappuccino" and source["water"] >= 250 and source["coffee"] >= 24 and
                    source["milk"] >= 100):
                print("Please insert coins.")
                Quarter = int(input("How many quarters?: "))
                Dime = int(input("How many dimes?: "))
                Nickle = int(input("How many nickles?: "))
                Penny = int(input("How many pennies?: "))
                insert_coins = Quarter * 0.25 + Dime * 0.1 + Nickle * 0.05 + Penny * 0.01
                if insert_coins >= price["cappuccino"]:
                    exchange = insert_coins - price["cappuccino"]
                    print(f"Here is ${exchange} in change.")
                    print("Here is your cappuccino ☕️ Enjoy!")
                    source["water"] -= Menu["cappuccino"]["ingredient"]["water"]
                    source["coffee"] -= Menu["cappuccino"]["ingredient"]["coffee"]
                    source["milk"] -= Menu["cappuccino"]["ingredient"]["milk"]
                    source["money"] += Menu["cappuccino"]["cost"]
                    [print(f"{key} : {value}") for key, value in source.items()]
                else:
                    print("Sorry that's not enough money. Money refunded.")
            elif selection == "cappuccino" and source["water"] < 250:
                print("Sorry there is not enough water.")
            elif selection == "cappuccino" and source["coffee"] < 24:
                print("Sorry there is not enough coffee.")
            elif selection == "cappuccino" and source["milk"] < 100:
                print("Sorry there is not enough milk.")

    # TODO: 7. Turn off-----------------------------------------------------------------------------------------------
    if selection == "off":
        turn_off = True
