def subtract_number(x,y):
    if y == 0:
        return x
    else:
        return subtract_number(x-1, y-1)
    
num1 = int(input())
num2 = int(input())

result = subtract_number(num1, num2)
print("The result of given question is :",result)