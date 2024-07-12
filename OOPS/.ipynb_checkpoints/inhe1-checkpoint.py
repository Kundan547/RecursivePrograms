class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def display(self):
        print(self.name, self.age)


class Stduent(person):
    def __init__(self, name, age):
        self.sName =  name
        self.sAge = age

        super().__init__('Kundan', age)

    def displayinfo(self):
        print(self.sName, self.sAge)

data = Stduent("Kuldeep", 23)
data.display()
data.displayinfo()
