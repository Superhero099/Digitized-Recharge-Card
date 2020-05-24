import sys
import random

"""
File: project.py
----------------------------------------------------------------
Title: Improvement on the traditional way of loading recharge cards
Case Study: Nigeria

Problems:
1. Users cannot load recharge card more than once.
2. Inability to produce recharge cards greater than N1000 (1000 Naira)

Thoughts:
1. What if you wanted to load about 40% of your recharge card? Impossible
2. Can multiple users load a single recharge card based on the value left after prior recharges on the recharge card?

Solutions:
1. A user can load a recharge card as much as he/she wants till the value is expended
2. Possibility of creating recharge cards worth N2000 and more
3. Multiple users on the same network can load the same recharge card and share the total value
"""

# dictionary contains recharge code and values
new_recharge = {}

# unique recharge card dictionary. contains only keys with unique values
unique_value = {}

# remainder of recharge card that was used
used_recharge = {}

# contains total loaded recharge balance
main_balance = {}


"""
Pre-Condition:
#1: None

Post-Condition:
#1: User is welcomed to the portal
"""
def welcome_note():
    print("Welcome to CodeInPlace Recharge Center, Nigeria")


"""
Pre-Condition:
#1: User is welcomed to the portal
#2. User is expected to enter an option to continue or exit

Post-Condition:
#1: The user is directed to another portal with lists of option to choose
"""
def code_input():
    code = input("Press *111# to begin or Press 0 to cancel: ")
    code = code.lower()
    exit_triggered(code)

    # if code != "*111#":
    #     sys.exit("Wrong Input! Thanks for using this service!")
    # print("")


def get_recharge_card_database():
    for i in range(1, 10):
        keys = random.randint(1000, 9999)
        values = i * 1000
        new_recharge[keys] = values
    new_database = new_recharge
    return new_database


"""
Pre-Condition:
#1: Lists all options available

Post-Condition:
#1: User inputs an option
"""
def first_response():
    while True:
        print("\n1. Buy Recharge Card")
        print("2. Load From Used Recharge Card")
        print("3. Check Balance")
        print("0 Quit | # Back | * Menu")

        choice = input("Reply: ")

        try:
            exit_triggered(choice)
            menu11(choice)

            if not choice.isdigit():
                sys.exit("Wrong Input! Thanks for using this service!")

            choice = int(choice)
            if choice > 3 or choice < 1:
                sys.exit("Invalid number! Thanks for using this service!")
        except ValueError:
            print("{0} is not supported" .format(choice))
        print("")
        return choice


"""
Pre-Condition:
#1: User is asked to pick a choice

Post-Condition:
#1: Based on User's choice module is redirected
"""
def action(response):
    if response == 1:
        dictionary_to_use = get_recharge_card_database()
        list_unique_recharge_cards(dictionary_to_use)
        choice = buy_recharge_card()
        process_buying_recharge(dictionary_to_use, choice)
    elif response == 2:
        dictionary_to_use = used_recharge
        list_recharge_cards(dictionary_to_use)
        choice = buy_recharge_card()
        process_buying_recharge(dictionary_to_use, choice)
    else:
        # response == 3:
        available_dictionary = used_recharge
        available_used(available_dictionary)

        balance_dictionary = main_balance
        balance_check(balance_dictionary)


"""
Pre-Condition:
#1: User selects "Buy Recharge" from the option 

Post-Condition:
#1: Filters new recharge code an places key and value in unique value dictionary
#2: Lists all recharge codes and value
"""
def list_unique_recharge_cards(dictionary):
    print("Select recharge card...")

    for key, value in sorted(dictionary.items(), key=lambda x: x[1]):
        if value not in unique_value.values():
            unique_value[key] = value

    # sorted_recharge_card = sorted(unique_recharge_card.items(), key=lambda x: x[1])
        # return unique_recharge_card
    for keys in unique_value.keys():
        print("Press " + str(keys) + " for N" + format(unique_value[keys], ',.2f'))


def list_recharge_cards(dictionary):
    print("Select recharge card...")
    for key in dictionary.keys():
        print("Press " + str(key) + " for N" + format(dictionary[key], ',.2f'))


"""
Pre-Condition:
#1: User selects option from menu items

Post-Condition:
#1 Depending on the user input, user is directed to particular module
"""
def buy_recharge_card():
    print("0 Quit | # Back | * Menu")

    choice = input("Reply: ")

    exit_triggered(choice)
    menu11(choice)

    if not choice.isdigit():
        sys.exit("Wrong Input! Thanks for using this service!")
    choice = int(choice)
    return choice


"""
Pre-Condition:
#1: User selects amount by recharge code
#2: Checks if recharge code is a available

Post-Condition:
#1 Updates all dictionaries by adding or subtracting amount loaded by user
"""
def process_buying_recharge(dictionary, choice):
    if choice not in dictionary:
        print(str(choice) + " is not among available recharge cards!")
    else:
        choice_value = dictionary[choice]
        print("\nYou have selected " + str(choice) + " for N" + format(choice_value, ',.2f'))
        print("0 Quit | # Back | * Menu")
        print("Enter amount from N50.00 to N" + format(choice_value, ',.2f') + " to recharge")
        amount_load = input("Reply: ")

        try:
            exit_triggered(amount_load)
            menu12(dictionary, amount_load)
            menu11_1(amount_load)

            # when removed, I get Value error
            if amount_load.isdigit():
                amount_load = int(amount_load)
                if 50 <= amount_load <= choice_value:
                    print("\nYour recharge of N" + format(amount_load, ',.2f') + " was successful!")
                    dictionary[choice] -= amount_load
                    print("Balance left from this recharge is N" + format(dictionary[choice], ',.2f'))

                    check_key(main_balance, choice, amount_load)

                    # if amount left is 0 remove key from available list of recharge cards
                    if dictionary[choice] == 0:
                        del dictionary[choice]
                    else:
                        used_recharge[choice] = dictionary[choice]
                        # remove recharge code from new recharge card and add to used list
                        if dictionary == new_recharge:
                            del dictionary[choice]
                else:
                    print("{0} is not in range".format(amount_load))
        except ValueError:
            print("{0} is not available".format(amount_load))
    # clear the unique value dictionary for another recharge operation
    unique_value.clear()

"""
Pre-Condition:
#1: User on particular transaction menu
#2: User presses 3 to check account balance

Post-Condition:
#1: Displays main balance 
#2: Adds all values in used_recharge dictionary
"""
def available_used(used):
    balance = 0
    for value in used.values():
        balance += value
    print("Available balance from used recharge cards is N" + format(balance, ',.2f'))
    return balance


"""
Pre-Condition:
#1: User on particular transaction menu
#2: User presses 3 to check account balance

Post-Condition:
#1: Displays main balance 
#2: Adds all values in balance dictionary
"""
def balance_check(used):
    balance = 0
    for value in used.values():
        balance += value
    print("Main Balance is N" + format(balance, ',.2f'))
    return balance


"""
Pre-Condition:
#1: User on particular transaction menu
#2: User presses 0, enter or "quit" to trigger closing the program

Post-Condition:
#1: Program closes
"""
def exit_triggered(choice):
    if choice == "0" or choice == "" or choice == "quit":
        sys.exit("Thanks for using this service!")


"""
Pre-Condition:
#1: User on particular transaction menu
#2: User presses # or * to go back to main menu

Post-Condition:
#1: Goes back to main menu
"""
def menu11(choice):
    if choice == "*" or choice == "#":
        while True:
            menu = first_response()
            action(menu)


"""
Pre-Condition:
#1: User on particular transaction menu
#2: User presses # or * to go back to main menu

Post-Condition:
#1: Goes back to main menu
"""
def menu11_1(choice):
    if choice == "*":
        menu = first_response()
        action(menu)


"""
Pre-Condition:
#1: User on as particular transaction menu

Post-Condition:
#1: Goes back to previous menu, the module that lists available recharge codes and value
"""
def menu12(dictionary, choice):
    if choice == "#":
        list_recharge_cards(dictionary)
        choice = buy_recharge_card()
        process_buying_recharge(dictionary, choice)


"""
Pre-Condition: 
#1: User finally loads a recharge card with any amount
#2: Checks if the key exists already
#3: If it does, add to the existing key value else create new key and value in balance or used_recharge dictionary

Post-Condition: 
#1: Value of key of a particular dictionary is added/updated 
"""
def check_key(dictionary, key, amount_load):
    if key in dictionary.keys():
        dictionary[key] += amount_load
        balance_check(main_balance)
    else:
        dictionary[key] = amount_load
        balance_check(main_balance)


"""
Pre-Condition: 
#1: Dictionary with several keys and values.
#2: Dictionary might include different keys with similar values

Post-Condition: 
#1: Returns a unique dictionary with unique values 
"""
def check_unique_recharge_value(dictionary):
    unique_recharge_card = {}

    for key, value in dictionary.items():
        if value not in dictionary.values():
            dictionary[key] = value
    return unique_recharge_card


def main():
    welcome_note()
    code_input()
    while True:
        response = first_response()
        action(response)


if __name__ == '__main__':
    main()
