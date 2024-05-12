#How to add two numbers in python
def add(a, b):
    sum = a + b
    return sum

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Values are Equal")
elif a % 2 == 1:
    print("The GIVEN VALUE OF A is odd Number:")
else:
    result = add(a, b)
print("The sum of given numbers is:", result)


#Add Two Numbers with User Input and string fromat

num1 = input()
num2 = input()

sum = float(num1) + float(num2)

print("The sum of {0} and {1} is {2}" .format(num1,num2, sum))