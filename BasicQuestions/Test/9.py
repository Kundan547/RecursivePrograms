"""Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320"""

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x = int(input())
print (fact(x))




#Second method for the program 
n = int(input()) 
                
fact = 1
i = 1
while i <= n:
    fact = fact * i;
    i = i + 1
print(fact)


# Method 3 using lambda function
n = int(input())
def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
print(shortFact(n))
