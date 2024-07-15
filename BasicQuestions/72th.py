def check_order(string, pattern):
	i, j = 0, 0
	for char in string:
		if char == pattern[j]:
			j += 1
		if j == len(pattern):
			return True
		i += 1

	return False
string = input("Enter a string: ")
pattern = input("Enter a pattren: ")
print(check_order(string, pattern))

