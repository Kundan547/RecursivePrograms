class Animal:
    categary = "Mamaal"

    def __init__(self, name, last):
        self.name = name
        self.last = last
        

    def speck(self):
        print(f"My name is {self.name}")

Tommy = Animal("Tommy")
Jacky = Animal("Jacky") 
Tommy.speck()
Jacky.speck()
