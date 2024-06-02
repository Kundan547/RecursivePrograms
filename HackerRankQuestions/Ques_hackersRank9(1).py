def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    
    if a == b:
        return a

#This is main logic of this program,
#here this process continues utill both a and b becomes equal.
    if a > b :
        return gcd(a-b,a)
    return gcd(a,b-a)

a = int(input())
b = int(input())
if (gcd(a,b)):
  print("The gcd of {0} and {1} is {2}",gcd(a,b))
else:
    print("Not found")
