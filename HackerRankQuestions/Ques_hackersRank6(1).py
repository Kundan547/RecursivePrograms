def product_numbers(x, y):
    if y == 1:
        return x
    elif x == 0 or y == 0:
        print("Error: One of the numbers is zero.")
        return 0  # Return 0 if either x or y is 0
    else:
        return x * product_numbers( x,y - 1)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = product_numbers(num1, num2)

print("The product of the given numbers is:", result)
