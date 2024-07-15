def Bubble_sort(Mylist):
    for i in range(len(Mylist)-1,0,-1):
        for j in range(i):
            if Mylist[j] > Mylist[j+1]:
                temp, Mylist[j] = Mylist[j], Mylist[j+1]
                Mylist[j+1] = temp

MyList = [23,11,32,5,90,54,78]
print(f"Elements of list brfore sorting:  {MyList}")

Bubble_sort(MyList)

print(f"Elements of list after sorting:   {MyList}")
