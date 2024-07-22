from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    def show_(self):
      #  self.brand = brand
      # self.model = model
        print("Every vehical has its own ways to run:")

    @abstractclassmethod
    def speed():
        pass


class Toyota(Vehicle):
    def speed(self):
        print("Speed is 130 km/h")

class Apache(Vehicle):
    def speed(self):
        print("Speed is 165 km/h")

class Thar(Vehicle):
    def speed(self):
        print("Speed is 175 km/h")


obj1 = Toyota()
obj1.speed()
obj1.show_()

