from operator import itemgetter

list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
#Here we are using sorted() to sort the list and get values form itemgetter() by giveing key.
print(sorted(list, key=itemgetter("age")))

#We can get  multiple values from itemgetter() by giving keys.
print(sorted(list, key=itemgetter("age","name")))

#we can get values in decending oredr by using reverse().
print(sorted(list, key=itemgetter("age"), reverse=True))