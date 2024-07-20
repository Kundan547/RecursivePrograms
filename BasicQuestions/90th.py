test_dict = {'Num1' : {"a" : 7, "b" : 9, "c" : 12},
             'Num2' : {"a" : 15, "b" : 19, "c" : 20}, 
             'Num3' :{"a" : 5, "b" : 10, "c" : 2}}

print("The original dictionary is : " + str(test_dict))
 
temp = "c"
 
res = [val[temp] for key, val in test_dict.items() if temp in val]
 
print("The extracted values : " + str(res)) 