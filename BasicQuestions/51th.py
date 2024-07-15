def Remove(duplicate):
	final_list = []
	for num in duplicate:
		if num not in final_list:
			final_list.append(num)
	return final_list
	
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))


#If you want to make it easy just convert it into set.
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(list(set(duplicate)))
print()


print(sorted(list(set(duplicate))))
