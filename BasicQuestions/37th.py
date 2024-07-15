#Excepation handling
a = input("Eter a number you want to  print: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invaild input!")

b = input("Enter a number :")
try:
    for i in range(1,11):
        if i%2 == 0:
            print(f"{(int(b))} is Even: ")
            break
        else:
            print("Its odd :")
except:
    print("Better luck next time!")