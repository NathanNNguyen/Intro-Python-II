class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}'
    
    def take(self, name):
        print(f"You have taken {self.name}")
    
    def drop(self, name):
        print(f"You have dropped {self.name}")