
sample_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}

sorted_dict = {}
for key in sorted(sample_dict, key=sample_dict.get):
	sorted_dict[key] = sample_dict[key]

print(sorted_dict)
