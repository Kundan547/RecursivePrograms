def Selection_sort(list):
    for i in range(len(list)-1):
        k = i # Smallest element.
        for j in range(i+1, len(list)):
            if (list[j] < list[k]):
                k = j
            if (k != j):
                temp = list[i]
                list[i] = list[k]
                list[k] = temp

list = [12,34,2,7,45,90,89,9,1]
print("Elements before sorting :")
print(list)

Selection_sort(list)
print("Elements after sorting :")
print(list)