def shift_right(list, num):
    n = len(list)
    num = num % n

    return list[-num:] + list[:-num]

num = int(input("Enter the number of positions to shift: "))
my_list = [1, 5, 2, 6, 7]

result = shift_right(my_list, num)

print("Sample Output:", result)