class  Details:
    def __init__(self, animal,group):
         self.animal = animal
         self.group = group

data = Details("Crab", "Crustacean")

print(f"{data.animal} belongs to the {data.group} group: ")


