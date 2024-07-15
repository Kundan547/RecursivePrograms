def check_duplicate(lst):
    dup_lst = []
    for i in lst:
        if i not in dup_lst:
            dup_lst.append(i)
        else:
            return True
    return False

lst = [4,2,5,7,4,2,1]
print(lst)
x = check_duplicate(lst)

print(x)
##new_list = set(lst)
##print(new_list)

lst1 = [1,2,3,4,5]
print(lst1)
x1 = check_duplicate(lst1)
print(x1)