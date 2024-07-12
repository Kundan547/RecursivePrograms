class Employee:
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            print('-->', emp.fullname())

dev1 = Developer('Kundan', 'Vyas', 50000, 'Python')
dev2 = Developer('Avinash', 'Vyas', 60000, 'Java')
dev3 = Developer('Lokesh', 'Singh', 45000, 'PHP')

mgr_1 = Manager('KD', 'SHRAMA', 90000, [dev1])
print(mgr_1.email)

mgr_1.add_emp(dev2)
mgr_1.add_emp(dev1)
#mgr_1.remove_emp(dev1)
mgr_1.add_emp(dev3)

print("Employees managed by {}:".format(mgr_1.fullname()))
for emp in mgr_1.employees:
    print('-->', emp.fullname())

