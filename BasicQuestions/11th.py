#Methods of sets
#Insertion in the set is done through the set.add() function.

People = {'Kunal','Barkat','Rahul'}

print("Peoples:", end=" ")
print(People)

#This will add new name in the set

People.add("Yuvraj")

#Adding elements to the set using iterator

for i in range(1,6):
    People.add(i)
print("\nSet after adding elements:", end=" ")
print(People)