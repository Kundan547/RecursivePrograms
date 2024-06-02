def square(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n*n
    
num = int(input("Enetr a number "))
print("The square of given number is ",square(num))