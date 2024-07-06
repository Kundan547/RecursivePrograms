class Person(object): 
	def __init__(self, name): 
		self.name = name 
		
	def getName(self): 
		return self.name 
	
	def isEmployee(self): 
		return False

class Employee(Person): 
	def __init__(self, name, eid): 

		''' In Python 3.0+, "super().__init__(name)" 
			also works'''
		super(Employee, self).__init__(name) 
		self.empID = eid 
		
	def isEmployee(self): 
		return True
		
	def getID(self): 
		return self.empID 

emp = Employee("Geek1", "E101") 
print(emp.getName(), emp.isEmployee(), emp.getID()) 
