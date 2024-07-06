class University:
    def __init__(self, College_Name, Occupation, Networth):
        self.College_Name = College_Name
        self.Occupation = Occupation
        self.Networth = Networth

    def info(self):
        print(f"{self.College_Name} is a {self.Occupation}")


data = University("Medicaps University", "Engineering College", 1000000)
data.info()

data.College_Name = "DAVV"
data.Occupation = "VinLinux"
data.info()