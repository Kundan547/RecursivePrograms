class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def info(self):
        print(f"{self.name} is a {self.occupation}.")

a = Person("Kundan", 21, "Software developer")
a.info()

a.name = "Kuldeep"
a.occupation = "Kindest"
a.info()