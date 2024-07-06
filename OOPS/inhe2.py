class Base(object):
  def __init__(self, name):
    self.name = name

  def getName(self):
    return self.name

# Inherited/sub class
class Child(Base):
  def __init__(self, name, age):
    Base.__init__(self, name)
    self.age = age

  def getAge(self):
    return self.age

# Inherited class from sub class above
class GrandChild(Child):
  def __init__(self, name, age, address):
    Child.__init__(self, name, age)
    self.address = address

  def getAddress(self):
    return self.address

g = GrandChild("James", 23, "Transylvania")
print(g.getName(), g.getAge(), g.getAddress())