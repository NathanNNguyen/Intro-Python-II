# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, location, inventory=[]):
        self.name = name
        self.location = location
        self.inventory = inventory
    
    def __str__(self):
        return {self.name}

    def move(self, direction):
        # check player's current location
        # if there is a room in specified direction, move there
        # if there isn't, print a msg specify that and not move 
        # the player
        att = direction + '_to'

        # Use `hasattr` function to check if a class has an attribute
        if hasattr(self.location, att):
            # if valid, use getattr to fetch the value associates with att
            # update self's location with the fetched room
            self.location = getattr(self.location, att) 
        else: 
            print("\nThere isn't a way there")
    
    def take_item(self, item):
        self.inventory.append(item)
        print(f"You picked up an {item}")

    def drop_item(self, item):
            self.inventory.remove(item)
            print(f"You dropped an {item}")
    
    def check_inventory(self):
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f'You have {item} in your inventory')
        else:
            print("Nothing in your inventory right now!")
    
    def inspect(self):
        for item in self.inventory:
            print(f'{item}')

    # def movement(self, direction):
    #     if direction == 'n':
    #         if self.current_room.n_to == None:
    #             print("There isn't a way there")
    #         else:
    #             self.current_room = self.current_room.n_to
    #     elif direction == 's':
    #         if self.current_room.s_to == None:
    #             print("There isn't a way there")
    #         else:
    #             self.current_room = self.current_room.s_to
    #     elif direction == 'w':
    #         if self.current_room.w_to == None:
    #             print("There isn't a way there")
    #         else:
    #             self.current_room = self.current_room.w_to
    #     elif direction == 'e':
    #         if self.current_room.e_to == None:
    #             print("There isn't a way there")
    #         else:
    #             self.current_room = self.current_room.e_to