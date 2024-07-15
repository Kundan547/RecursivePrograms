def list_even_numbers(start, end):
    result_list = []
    for number in range(start, end):
        if number % 2 == 0:
            result_list.append(number)
    return result_list

print(list_even_numbers(10,20))