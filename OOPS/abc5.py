import abc

class parent:       
    def data(self):
        pass

class child(parent):
    def data(self):
        print("child class")

print( issubclass(child, parent))
print( isinstance(child(), parent))