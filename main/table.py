def table(x):
    """
    Print the multiplication table of the given number.

    Parameters:
        x (int): The number for which the multiplication table will be printed.

    Returns:
        None: This function does not return any value.
    """    
    # Loop through numbers from 1 to 10
    for i in range(1, 11):
        # Calculate the product of x and the current number (i)
        product = x * i
        # Print the multiplication table entry for x and i
        print(f"{x} x {i} = {product}")

# Prompt the user to input the value of x
x = int(input("Enter value of x: "))

# Call the 'table' function with the user-provided value of x
table(x)
