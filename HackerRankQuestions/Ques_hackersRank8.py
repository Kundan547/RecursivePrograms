#program to find factorial of given number

def fact(n):
    return 1 if (n ==1 or n == 0)else n * fact(n-1)


num = int(input())
print("The factorial of ",num,"is",fact(num))