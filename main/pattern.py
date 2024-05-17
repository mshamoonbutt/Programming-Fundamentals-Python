def pattern(num_rows, max_num):
    """
    Print a pattern with increasing numbers up to a maximum number in each row.

    Args:
    num_rows (int): The number of rows in the pattern.
    max_num (int): The maximum number to print in each row.

    Returns:
    None
    """
    # Loop to print the pattern
    for i in range(1, num_rows + 1):
        for j in range(1, i + 1):
            # Check if j is greater than max_num, and print max_num if true
            if j > max_num:
                print(max_num, end="")
            else:
                print(j, end="")
        # Move to the next line after each row
        print()

# Input the number of rows and the maximum number
num_rows = int(input("Enter the number of rows: "))
max_num = int(input("Enter the maximum number: "))

pattern(num_rows, max_num)