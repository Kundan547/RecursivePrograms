def merge(dict1, dict2):
    return (dict1.update(dict2))

dict1 = {'Name':'Kundan', 'Age':22}
dict2 = {'Email':'Test123@gmail.com', 'Number':'123456789'}

print(merge(dict1, dict2))

print(dict1)

print()
print("Tring something new")
#for key, value in merge.items():
 #   print(key, value)

#print(dict1['Name'])

# Tring to add both dictionary in another dictionary.

dict3 = {**dict1 , **dict2}
print(dict3)
