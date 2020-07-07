# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def __str__(self):
        return {self.name}
    
    def locate(self):
        print(f'You are now in {self.current_room}.') 
    
    def movement(self, direction):
        if direction == 'n':
            if self.current_room.n_to == None:
                print("There isn't a way there")
            else:
                self.current_room = self.current_room.n_to
        elif direction == 's':
            if self.current_room.s_to == None:
                print("There isn't a way there")
            else:
                self.current_room = self.current_room.s_to
        elif direction == 'w':
            if self.current_room.w_to == None:
                print("There isn't a way there")
            else:
                self.current_room = self.current_room.w_to
        elif direction == 'e':
            if self.current_room.e_to == None:
                print("There isn't a way there")
            else:
                self.current_room = self.current_room.e_to