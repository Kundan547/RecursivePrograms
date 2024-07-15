# Python program to demonstrate intersection of two sets

set1 = set()
set2 = set()

for i in range(5):
	set1.add(i)

for i in range(3,9):
	set2.add(i)

# Intersection using intersection() function
set3 = set1.intersection(set2)

print("Intersection using intersection() function")
print(set3)

# Intersection using "&" operator
set3 = set1 & set2

print("\nIntersection using '&' operator")
print(set3)

set4 = set()
set3
for i in range(0,5):
	set4.add(i)

set5 = set3.intersection(set4)
print(set5)