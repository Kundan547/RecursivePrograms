#First missing number
def findMissingNumber1(array1, array2):
    array1.sort()
    array2.sort()
    for num1, num2 in zip(array1, array2):
        if num1!=num2:
            return num1
    return array1[-1]