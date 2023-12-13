from __future__ import annotations


class Item:
    items_list = []

    def __init__(self, title: str, item_type: str, date_added: int, date_of_manufacture: int, description: str):
        self.title = title
        self.type = item_type
        self.date_added: float = date_added
        self.date_of_manufacture: float = date_of_manufacture
        self.description: str = description
        Item.items_list.append(self)


def show_menu():
    while True:
        print('-------------------------')
        print('Retro Technology Collector')
        print('-------------------------')
        print('1. Add Item to Collection.')
        print('2. Show Items in the Collection.')
        print('3. Edit An Item in the Collection.')
        print('4. Delete Items in the Collection.')
        print('5. Exit')
        response = input('Choice> ')

        if response == '1':
            add_item()
        elif response == '2':
            show_items()  # TODO
        elif response == '3':
            edit_items()  # TODO
        elif response == '4':
            delete_items()  # TODO
        elif response == '5':
            break
        else:
            print('Invalid Choice!\n')


def add_item():
    print('')
    title = input('Title> ')
    item_type = input('Types : 1. Computer, 2. Camera, 3. Phone, 4. Video Player\nType> ')
    possible_types = ["1", "2", "3", "4"]

    if item_type not in possible_types:
        print('Invalid Input!, please enter either 1 , 2 , 3 or 4')
        return
    date_added = input('Date Added> ')
    date_of_manufacture = input('Date of Manufacture> ')
    description = input('Description> ')
    print('')
    Item(title, item_type, int(date_added), int(date_of_manufacture), description)


def show_items():
    print('Item\tType\tDate Added\tDate of Manufacture')
    for item in Item.items_list:
        print(f'{item.title}\t{item.type}\t{item.date_added}\t{item.date_of_manufacture}')


show_menu()
