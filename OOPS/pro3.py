class Animal:
    categary = "Mamaal"

    def __init__(self, name):
        self.name = name

    def speck(self):
        print(f"My name is {self.name}")

Tommy = Animal("Tommy")
Jacky = Animal("Jacky") 
Tommy.speck()
Jacky.speck()
