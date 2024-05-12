#Add Two Number Using Lambda Function

add_numers = lambda a , b : a + b
prod_number = lambda a , b : a * b
num1 = int(input())
num2 = int(input())

result = add_numers(num1,num2)
print("The sum of gievn numbers is : ",result)

print() 

num3 = int(input())
num4 = int(input())
result = prod_number(num3,num4)


print("The sum of gievn numbers is : ",result)
