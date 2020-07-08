from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['bow']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['sword']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['knife']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['sword']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['gun']),
}

item = {
    'sword': Item('Infinity Edge', 'Best of the best'),
    'gun': Item('AWP', 'Eagle Eye'),
    'knife': Item('Valyrian', 'White walker killer'),
    'bow': Item('Crossbow', 'Dragon killer')
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# user = int(input("[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n"))
user = input('What is your name: ')
player = Player(user, room['outside'])
print(f'Welcome to the game {player.name}! Make your movements carefully.')
print('Use the following commands for the game:')
print('[n] North [s] South [w] West [e] East [q] Quit')
print('[i] Check inventory [t] Take item [d] Drop item')
# Write a loop that:
while True:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
    # print('\n')
    print(player.location)
    print(f'Available items: {player.location.item[0]}')

# * Waits for user input and decides what to do.
    console = input('\nCommand: ')

# If the user enters "q", quit the game.
    if console == 'q':
        print('Thanks for playing!')
        break

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    if console == 'n':
        # move north
        player.move(console)
        
    elif console == 's':
        # move north
        player.move(console)
        
    elif console == 'w':
        # move north
        player.move(console)
        
    elif console == 'e':
        # move north
        player.move(console)
    elif console == 't':
        player.take_item(player.location.item[0])
    elif console == 'd':
        player.drop_item(player.inventory[0])
    elif console == 'i':
        player.check_item()
        