from abc import ABC, abstractclassmethod

class Car(ABC):
    def show(self):
        print("Every car has 4 wheels: ")
    @abstractclassmethod
    def speed():
        pass



class Toyota(Car):
    def speed(self):
        print("Speed is 120km/h: ")

class Mahindra(Car):
    def speed(self):
        print("Speed is 150 km/h: ")


class Thar(Car):
    def speed(self):
        print("Spped is 170 km/h: ")


#Because of abstractmethod we dont have the access to 
# the parent class so we need to create object from child class
#To perform changes or create  something new.

obj1 = Toyota()
obj1.show()
obj1.speed()

obj2 = Mahindra()
obj2.show()
obj2.speed()


obj3 = Thar()
obj3.show()
obj3.speed()

# Program executed succesfully.