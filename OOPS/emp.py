class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@company.com'


    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Tilak', 'Vyas', 25000)
emp2 = Employee('Karthik', 'Vyas', 55000)


print(emp1.email)
print(emp2.email)

print(emp1.fullname())
print(emp2.fullname())

print(emp2.pay)