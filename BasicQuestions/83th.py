class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_rasie_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6 :
            return False
        return True


emp1 = Employee('Kundan', 'Vyas', 50000)
emp2 = Employee('Maan', 'Singh', 50000)


Employee.set_rasie_amt(1.05)

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

emp_str_1 = 'kunal-verma-25000'
emp_str_2 = 'Karthik -vyas-50000'
emp_str_3 = 'Trilok-vyas-90000'

new_emp_1 = Employee.from_string(emp_str_1)


print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016,2,2)

print(Employee.is_workday(my_date))