country_code = {'India' : '0091',
				'Australia' : '0025',
				'Nepal' : '00977'}

# search dictionary for country code of India
print(country_code.get('India', 'Not Found'))

# search dictionary for country code of Japan
print(country_code.get('Japan', 'Not Found'))


#PopItem() method in dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem() # its popup the year block.
car.pop("brand") # this one popup the brand block.

print(car)


#Del() method in dictionary in python#
#del car
del car["model"] # Now we are delete the model block
print(car)# Now the dictionary isd empty