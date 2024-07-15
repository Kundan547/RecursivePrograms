#Accessing elements form Dictionary.
dict = {1:'kundan', 2:'kuldeep', 3:'karthik', 4:'trilok'}
print(dict)

print(dict[1])
print(dict[3])
print(dict[2])

#ACCESS THE VALUE FROM THE DICTIONAY.
print(dict.get(4))


#Delete a element from Dictionay using DEL.

del(dict[3])
print(dict)