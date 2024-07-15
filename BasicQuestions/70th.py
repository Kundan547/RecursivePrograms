class Animal:
    alive = True
    
    def eat(self):
        print("This animal is eating.")
    
    def sleep(self):
        print("This animal is sleeping.")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running.")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming.")

class Bird(Animal):
    def fly(self):
        print("This bird is flying.")

rabbit = Rabbit()
fish = Fish()
bird = Bird()

bird.fly() 
rabbit.run()
fish.swim()
