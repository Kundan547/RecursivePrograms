#Zip() function in python

name = ("Kundan", "Kuldeep", "Trilok")
location = ("Hell", "Heaven", "Heaven")

#convert into dictionary.
zipped = dict(zip(name, location))
print(zipped)

#Convert into list.
zipped = list(zip(name, location))
print(zipped)

#Convert into tuple.
zipped = tuple(zip(name, location))
print(zipped)

#Convert into set.
zipped = set(zip(name, location))
print(zipped)