a = int(input())
b = int(input())

maximum = lambda a,b:a if a > b else b
print(f'{maximum(a,b)} is a maximum of number')


#Using list 
a=2;b=4
x=[a if a>b else b] 
print("maximum number is:",x)

#Using sorting to find the maximum element
a = 32
b = 14
x=[a,b]
x.sort()
print(x[-1])
