def traverse(my_list, value):
    exists = False
    for i in my_list:
        if i == value:
            exists = True
            break

    if exists:
        print(f"{value} exists in the list.")
    else:
        print(f"{value} does not exist in the list.")

my_list = [1, 3, 5, 7]
value = int(input("Enter value to check: "))
traverse(my_list, value)