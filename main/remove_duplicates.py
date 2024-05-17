def remove_duplicates(input_list):
    result_list = []
    for num in input_list:
        if num not in result_list:
            result_list.append(num)
    return result_list

input_list = [1, 2, 1, 3, 2, 3, 4]

result_list = remove_duplicates(input_list)

print(result_list)