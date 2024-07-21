class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'


    def fullname(self):
        return'{} {}'.format(self.first, self.last)
    

emp1 = Employee('Kundan', 'Vyas')
print(emp1.fullname())
print(emp1.email)
print(emp1.first)
