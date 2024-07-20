test_dict = {'val1': {'a': 7, 'b': 9, 'c': 12},
			'val2': {'a': 15, 'b': 19, 'c': 20},
			'val3': {'a': 5, 'b': 10, 'c': 2}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

temp = "c"

res = []

for value in test_dict.values():
	
	# checking if key exists in current value
	if temp in value:
		
		# appending value of key to the result list
		res.append(value[temp])

print("The extracted values : " + str(res))
