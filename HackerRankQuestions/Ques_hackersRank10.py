def multiply_recursive(x, y):
    # Base case: if one of the numbers is 0, return 0
    if x == 0 or y == 0:
        return 0
    # Base case: if one of the numbers is 1, return the other number
    elif x == 1:
        return y
    elif y == 1:
        return x
    # Recursive case: multiply x by (y-1) and add x to the result
    else:
        return x + multiply_recursive(x, y - 1)

x = int(input())
y = int(input())

result = multiply_recursive(x, y)
print("Result:", result) 
