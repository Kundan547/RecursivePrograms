def add_numbers(x,y):
    if y == 0:
        return x
    else:
        return add_numbers(x+1,y-1)

num1 = int(input())
num2 = int(input())

result = add_numbers(num1,num2)
print("The sum of given numbers is : ",result)