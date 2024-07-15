def findsum(arr):
    l = []

    for i in arr:
        l.append(i + arr[i])

    print(*l)

arr = {1:10, 2:20, 3:30, 4:40, 5:50}
findsum(arr)