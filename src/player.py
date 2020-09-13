# Write a class to hold player information, e.g. what room they are in currently.

from item import Item

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    # List player's inventory
    def print_inventory(self):
        if len(self.inventory) == 0:
            print("\nThe player's inventory is empty.")
        else:
            print("\nHere is the player's inventory:")
            for i, item in enumerate(self.inventory):
                print(f'   {i+1}: {item}')

    # Used when player takes an item
    def on_take(self, take_item):
        print(f'You have picked up {take_item}.')

    # User when player drops an item
    def on_drop(self, drop_item):
        print(f'You have dropped {drop_item}.')

    # User takes an item in the room
    def take(self, take_item):
        room_items_names = [item.name for item in self.current_room.items]
        if take_item not in room_items_names:
            print(f'\nERROR: {take_item} is not located in the room.')
        else:
            for item in self.current_room.items:
                if take_item == item.name:
                    self.inventory.append(item)
                    self.current_room.items.remove(item)
                    self.on_take(take_item)
                    break

    # User drops an item in the room
    def drop(self, drop_item):
        inventory_items_names = [item.name for item in self.inventory]
        if drop_item not in inventory_items_names:
            print(f'\nERROR: {drop_item} is not located in players inventory.')
        else:
            for item in self.inventory:
                if drop_item == item.name:
                    self.inventory.remove(item)
                    self.current_room.items.append(item)
                    self.on_drop(drop_item)
                    break
