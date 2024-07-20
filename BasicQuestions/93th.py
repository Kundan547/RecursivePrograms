test_list = [{'Name' : 'Apple', 'Price' : 18, 'Color' : 'Red'},
             {'Name' : 'Mango', 'Price' : 20, 'Color' : 'Yellow'},
             {'Name' : 'Orange', 'Price' : 24, 'Color' : 'Orange'},
             {'Name' : 'Plum', 'Price' : 28, 'Color' : 'Red'}]
 
print("The original list is : " + str(test_list))
 
val_list = ['Yellow', 'Red', 'Orange', 'Green']
 
key = 'Color'
 
res = [any(clr == sub[key] for sub in test_list) for clr in val_list]

print("The Association list in Order : " + str(res)) 