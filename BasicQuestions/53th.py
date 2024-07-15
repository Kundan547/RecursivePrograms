def RemoveDublicate(data):
    final_list = []
    for num in data:
        if  num not in final_list:
            final_list.append(num)
    return final_list        

data = [2,3,4,5,5,6,3,2,1]
print(RemoveDublicate(data))