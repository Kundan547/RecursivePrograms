def list_odd_number(start, end):
    result_list=[]
    for number in range(start, end):
        if number % 2 == 1:
            result_list.append(number)

            result_list.sort()

            result_list.reverse()
    return result_list

print(list_odd_number(10,20))
