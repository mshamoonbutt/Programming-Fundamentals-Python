def print_left_right(left_str, right_str):
    """
    Prints two strings on one line with left-justified and right-justified text,
    separated by periods to fill a 50-character line.

    Args:
    left_str (str): The first string to be left-justified.
    right_str (str): The second string to be right-justified.

    Returns:
    None: Prints the formatted line with the two input strings.
    """
    # Calculate the number of periods needed to pad the string to a length of 50 characters
    num_periods = 50 - len(left_str) - len(right_str)

    # Construct the final string by concatenating left_str, a string of num_periods periods, and right_str
    result = f"{left_str}{'.' * num_periods}{right_str}"

    # Print the constructed string
    print(result)


# Get user input
left_str = input("Enter first string: ")
right_str = input("Enter second string: ")

# Call the print_left_right function with the user input
print_left_right(left_str, right_str)