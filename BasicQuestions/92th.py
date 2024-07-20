test_dict = {"Akshat": [1, 4, 5, 3],
			"Nikhil": [4, 6],
			"Akash": [5, 2, 1]}

test_list = [2, 1]

# printing original dict
print("The original dictionary : " + str(test_dict))

# printing original list
print("The original list : " + str(test_list))
res = dict()
for i in test_dict.keys():
	c = 0
	for j in test_list:
		c += test_dict[i].count(j)
	res[i] = c
# print result
print("The summation of element occurrence : " + str(res))
