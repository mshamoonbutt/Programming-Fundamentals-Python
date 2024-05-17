def are_lists_equal(list1, list2):

    for i in range(len(list1)):
        if int(list1[i]) != int(list2[i]):
            return False

    return True

L1 = [1, 2, 3, 4.4]
L2 = [1, 2, 3, 4]

if are_lists_equal(L1, L2):
    print("Sample Output 1: Equal")
else:
    print("Sample Output 1: Not equal")

L1 = [1, 2, 3, 4, 4]
L2 = [1, 2, 4, 3, 4]

if are_lists_equal(L1, L2):
    print("Sample Output 2: Equal")
else:
    print("Sample Output 2: Not equal")