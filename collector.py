from __future__ import annotations
from datetime import datetime


class Item:
    items_list = []

    def __init__(self, title: str, item_type: str, date_added, date_of_manufacture, description: str):
        self.title = title
        self.type = item_type
        self.date_added: datetime = datetime.strptime(date_added, "%Y/%m/%d")
        self.date_of_manufacture: datetime = datetime.strptime(date_of_manufacture, "%Y/%m/%d")
        Item.items_list.append(self)

    def __str__(self):
        added = self.date_added.strftime("%Y/%m/%d")
        manufacture = self.date_of_manufacture.strftime("%Y/%m/%d")
        return f'{self.title}\t{self.type}\t{added}\t{manufacture}'


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
            show_items()
        elif response == '3':
            edit_items()
        elif response == '4':
            delete_items()
        elif response == '5':
            break
        else:
            print('Invalid Choice!\n')


def add_item():
    print('')
    title = input('Title> ')
    item_type = input('Types : Computer, Camera, Phone, Video Player\nType> ').capitalize()
    possible_types = ['Computer', 'Camera', 'Phone', 'Video Player']

    if item_type not in possible_types:
        print('Invalid Input! please enter either Computer, Camera, Phone or Video Player')
        return
    date_added = input('Date Added> ')
    date_of_manufacture = input('Date of Manufacture> ')
    description = input('Description> ')
    print('')
    print('Item Added Successfully!')
    Item(title, item_type, date_added, date_of_manufacture, description)


def show_items():
    print('{0:10}\t{1:10}\t{2:10}\t{3:10}'.format('Item', 'Type', 'Date Added', 'Date of Manufacture'))
    for item in Item.items_list:
        # Format dates for display
        added = item.date_added.strftime("%Y/%m/%d")
        manufacture = item.date_of_manufacture.strftime("%Y/%m/%d")
        print('\t'.join([item.title.ljust(10), item.type.ljust(5), added, manufacture]))


def edit_items():  # TODO
    pass


def delete_items():
    print('')
    deleting = input('Enter the the item you want to delete: ')
    for item in Item.items_list:
        if item.title == deleting:
            Item.items_list.remove(item)
            print(f'Item "{deleting}" deleted successfully!')
            return
        else:
            print(f'Item "{deleting}" not found in the collection.')


show_menu()
