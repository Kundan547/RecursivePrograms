#Demonstrate how to parent constructors are called

#Parent class
class Person(object):

    def __init__(self, name , idnumber):
        self.name = name 
        self.idnumber = idnumber

    def dispaly(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print(f"My name is {self.name}")
        print(f"Idnumber: {self.idnumber}")


#Chlid class

class employee(Person):
    def __init__(self, name, idnumber, salary, post) -> list: 
        self.salary = salary
        self.post = post

        Person.__init__(self, name, idnumber)

    def details(self):
        print(f"My name is {self.name}")
        print(f"IdNumber: {self.idnumber}")
        print(f"Post: {self.post}")


emp1 = employee("kundan", 487951, 200000, "Intern")

emp1.dispaly()
emp1.details()