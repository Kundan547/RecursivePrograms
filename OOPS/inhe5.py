class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)
    
class Student(Person):
    def __init__(self, name, age):
        self.sName = name
        self.sAge = age
        super().__init__("Kuldeep", '19')

    def displayInfo(self):
        print(self.sName, self.sAge)

obj = Student("Kundan", 22)
obj.display()
obj.displayInfo()
