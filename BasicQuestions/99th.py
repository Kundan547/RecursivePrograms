def unique(list1):

    unique_list = []

    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print (x)


# driver code
list1 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is")
unique(list1)


list2 = [1, 2, 1, 1, 3, 4, 3, 3, 5]
print("\nthe unique values from 2nd list is")
unique(list2)
