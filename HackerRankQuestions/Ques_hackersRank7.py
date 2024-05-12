#Find Maximum of two numbers in Python

def maximum(a,b):
    if a >= b :
        return a
    else:
        return b
    
num1 = int(input())
num2 = int(input())
print("The maximum number of given values is :")
print(maximum(num1,num2))