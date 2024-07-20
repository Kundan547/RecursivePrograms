import sys

l1 = [9,1,8,2,7,3,6,4,5]
s_l1 = sorted(l1)

size_l1 = sys.getsizeof(l1)
size_s_l1 = sys.getsizeof(s_l1)

print(f"Size of l1: {size_l1} bytes")
print(f"Size of s_l1: {size_s_l1} bytes")

if size_l1 == size_s_l1:
    print("Both lists have the same size")
elif size_l1 > size_s_l1:
    print("l1 is larger than s_l1")
else:
    print("s_l1 is larger than l1")