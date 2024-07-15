list1 = [3,2,17,4,8,97,88,39]
print("list1= ",list1)

lst = []

print("Prime Numbers from the list are as follows: ")

for a in list1:
    prime = True
    for i in range(2,a):
        if(a%i == 0):
            prime = False
            break
    if prime:
        lst.append(a)
print(lst)