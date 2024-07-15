#Linear Search algorithm.

def Linear_Search(data, key):
    for i in range(len(data)):
        if (data[i] == key):
            print(key, "is found at index", i)
            return i
            break
    return -1


data = [12,23,42,54,65]    
print(data)

key = int(input("Enter a number to be searched: "))

l1 = Linear_Search(data, key)
if (l1 != -1):
    print(key, "is found at position", l1+1)
else:
    print(key, "is not present in the list")