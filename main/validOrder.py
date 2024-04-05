def check_order(a, b, c):
    """
    Check the order of three integers.

    Args:
    a, b, c (int): The three integers to be checked.

    Returns:
    None: Prints "in order" if sorted in ascending or descending order, or "not in order" otherwise.
    """
    if a < b < c or a > b > c:
        print("in order")
    else:
        print("not in order")

# Take Input:
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))

# Call the function
check_order(a, b, c)