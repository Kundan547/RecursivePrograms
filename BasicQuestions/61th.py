def is_list_palindrome(lst):
    r = lst[::-1]
    for i in range(0, (len(lst)+1)//2):
        if r[i] != lst[i]:
            return False
    return True

lst = [1,2,3,2,1]
x = is_list_palindrome(lst)
print(lst, "(Is palindrome :)", x)

lst1 = [1,2,3,4]
x1 = is_list_palindrome(lst1)  
print(lst1, "(Is palindrome :)", x1)

lst2 = [1,5,1,5,1]
x2 = is_list_palindrome(lst2)  
print(lst2, "(Is palindrome :)", x2)