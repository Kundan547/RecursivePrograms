def returnsum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i

    return sum

dict = {'a': 100,
        'b': 185,
        'c':250,
        'd':300
        }
print(dict)
print("Sum of given  dictionary: ",returnsum(dict))

print()

def returnSum(dict1):
    return sum(dict1.values())
 #Here we are using sum() to get the sum of dictionaries values.
dict1 = {'a': 100, 'b': 200, 'c': 300}
print(dict1)
print("Sum of given dictionary: ", returnSum(dict1))