#Sum of dictionary
def returnSum(myDict):

	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)

	return final

dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))
