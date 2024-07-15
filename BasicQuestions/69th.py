def Insertion_sort(list):
    for i in range(1, len(list)):
        CurrentElement = list[i]
        k = i -1

        while k >= 0 and list[k] > CurrentElement:
            list[k+1] = list[k]
            k = k-1

        list[k+1] = CurrentElement

list = [12,23,5,2,21,1,4]
print("Elements before sorting")
print(list)

Insertion_sort(list)
print("Elements after sorting :")
print(list)