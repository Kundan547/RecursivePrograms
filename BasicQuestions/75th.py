def merge(dict1, dict2):
    for i in dict2.keys():
        dict1[i] = dict2[i]
    return dict1

dict1 = {'Name': 'Kundan', 'Age': 21}
dict2 = {'Email': 'test123@gmail.com', 'Phone':123456789}

dict3 = merge(dict1, dict2)

print(dict3)