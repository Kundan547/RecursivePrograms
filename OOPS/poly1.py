class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  def move(self):
    return super().move()

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a class object
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747") 

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()