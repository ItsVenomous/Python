from __future__ import annotations
import sys


def show_menu():
    while True:
        print('-------------------------')
        print('Welcome To McLeos!')
        print('-------------------------')
        print('1. Show Menu')
        print('2. Place your order')
        print('3. Exit')

        response = input('Choice> ')  # Asking for the user's input

        if response == '1':
            show_food_menu()
        elif response == '2':
            place_order()
            sys.exit()
        elif response == '3':
            print('See You Next time!')
            sys.exit()  # Terminate the program
        else:
            print('Invalid Choice!\n')  # Print invalid choice if the customer didn't enter one of the options


def show_food_menu():
    # Display the menu to the customer
    print('Main Courses:')
    print('')
    print('Cheeseburger - 10 Euros')
    print('Nachos - 6 Euros')
    print('Pizza - 6 Euros')
    print('')
    print('Drinks:')
    print('')
    print('Coke - 5 Euros')
    print('Water - 4 Euros')


def place_order():
    order = input('Place Your Order>').casefold()  # User input for the customer asking to place the order
    items = order.split()
    price = 0
    for item in items:
        if item == 'cheeseburger':
            price += 10
        elif item in ['nachos', 'pizza']:
            price += 6
        elif item == 'coke':
            price += 5
        elif item == 'water':
            price += 4
        else:
            price += 5

    # Displaying the final price, Rounding to reduce the decimal places to 2
    print('Price:', round(price, 2), 'Euros')
    print('Tax:', round(price*0.07, 2), 'Euros')
    print('--------------------------------------------')
    print('The total cost for your order is', round(price * 1.07, 2), 'Euros!')


if __name__ == "__main__":
    show_menu()
