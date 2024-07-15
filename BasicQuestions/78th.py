test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}

print("The original dictionary is : " + str(test_dict))
 
res = {}
for i in range(len(test_dict['month'])):
    res[test_dict['month'][i]] = test_dict['name'][i]

print("Updated dictionary : " + str(res))