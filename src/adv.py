import textwrap
from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    [Item('Gold', 'All that glitters isnt gold'), Item('Key', 'This will unlock your hearts desire ')]),
    'foyer': Room("Foyer",
                  "Dim light filters in from the south. Dusty passages run north and east.",
                  [Item('Silver', 'You won the silver!'), Item('Sword', 'Thrust this into your enemies')]),
    'overlook': Room("Grand Overlook",
                     "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.",
                     [Item('Bronze', 'Too bad its not gold or silver'), Item('Dagger', 'Use this to stab your enemies in the back')]),
    'narrow': Room("Narrow Passage",
                   "The narrow passage bends here from west to north. The smell of gold permeates the air.",
                   [Item('Book', 'Better catch up on your reading.'), Item('Wand', 'If only you had a spellbook...')]),
    'treasure': Room("Treasure Chamber",
                     "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
                     [Item('Chest', 'No soup for you!')]),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Make a new player object that is currently in the 'outside' room.
player = Player("John Doe", room['outside'])

while True:

    # Print current room
    print("\nCurrent room:", player.current_room.name)

    # Print room description
    wrapper = textwrap.TextWrapper(width=50)
    word_list = wrapper.wrap(text=player.current_room.description)
    for element in word_list:
        print('   ', element)

    # Print items available to user in room
    if len(player.current_room.items) == 0:
        print('There are no items available in the room.')
    else:
        print("These items are available in the room:")
        for i, item in enumerate(player.current_room.items):
            print(f'   {i+1}: {item}')

    # Request user input
    print(
        "Where to?\n   1. [n] North\n   2. [e] East\n   3. [s] South\n   4. [w] West\n   5. [i] Inventory\n   6. 'take' [item]\n   7. 'drop' [item]\n   8. [q] quit")
    selection = input(">>> ").split(" ")

    # Case: User quits game
    if selection[0] == 'q':
        print('\nFarewell!')
        break

    # Print player's inventory
    if selection[0] == 'i':
        player.print_inventory()

    # Case: User moves to new room
    elif len(selection) == 1 and selection[0] in ['n', 'e', 's', 'w']:

        # Confirm user entered valid directions in current room
        if (player.current_room == room['outside'] and selection[0] in ['n']) or \
            (player.current_room == room['foyer'] and selection[0] in ['s', 'n', 'e']) or \
            (player.current_room == room['overlook'] and selection[0] in ['s']) or \
            (player.current_room == room['narrow'] and selection[0] in ['w', 'n']) or \
            (player.current_room == room['treasure'] and selection[0] in ['s']):

            # Move player to new current room
            if selection[0] == 'n':
                player.current_room = player.current_room.n_to
            if selection[0] == 'e':
                player.current_room = player.current_room.e_to
            if selection[0] == 's':
                player.current_room = player.current_room.s_to
            if selection[0] == 'w':
                player.current_room = player.current_room.w_to
        else:
            print("\nERROR: Player cannot move in that direction from this room.")

    # Case: User picks up or drops item in room
    elif len(selection) == 2:

        # Case: User picks up item
        if selection[0] == 'take':
            player.take(selection[1])

        # Case: User drops item
        elif selection[0] == 'drop':
            player.drop(selection[1])

        # Case: Invalid action
        else:
            print('\nERROR: Invalid action!')

    # Case: User enters invalid selection
    else:
        print('\nERROR: Invalid selection!')
