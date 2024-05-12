def hcf(a,b):
    if (b == 0):
        return a
    else:
        return hcf(b, a%b)

num1 = int(input())
num2 = int(input())

print("The gcd of {0},{1} is {3} ",hcf(num1,num2))