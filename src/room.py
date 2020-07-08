# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, item=[]):
        self.name = name
        self.description = description
        self.item = item

    def __str__(self):
        return f'\nCurrently in {self.name} ({self.description}).'

    # def check_i(self):
    #     for i in self.item:
    #         if i:
    #             print(f'There is a {i} in this room, would you want to take it? (y/n)')
    #         else:
    #             print(f"There isn't any good here :(")
            
    def add_i(self, item):
        self.append(item)

    def remove_i(self, item):
        self.remove(item)