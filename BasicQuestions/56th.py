#Binary Search
def binary_search(data, key):
    low = 0
    high = len(data) - 1
    while low<=high:
        mid = (low+high)//2
        if data[mid]==key:
            return mid
        elif key > data[mid]:
            low = mid + 1
        else:
            high = mid -1
    return -1
data = [12,33,45,67,89,90] 
print(data)

key = int(input("Enter the number to search: "))
x = binary_search(data,key)

if(x == -1):
    print(f"{key} is not present in the list: ")
else:
    print(f"The element {key} is found at position {x+1}: ")