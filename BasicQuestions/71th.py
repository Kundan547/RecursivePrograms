Student = {'name': 'Kundan', 'age': 23, 'courses':['Math', 'Science']}
#print(Student)

#print(Student['name'])
#print(Student['age'])
#print(Student['courses'])
print(Student)

Student['Phone'] = '123456789'
Student['name'] = 'Kuldeep'

print(Student)


#Insted of doing this we can use this.

Student.update({'name':'Kuldeep', 'age': 20, 'courses':['Math', 'Science', 'hindi']})
print(Student)

#del Student['age']

age = Student.pop('age')
print(Student)
print(age)