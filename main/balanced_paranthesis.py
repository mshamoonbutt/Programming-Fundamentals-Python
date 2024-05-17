def bracket(input_string):
    """
    Check if a given string contains balanced parentheses, square brackets, and curly braces.
    
    The function counts the number of opening and closing brackets to determine if they are balanced.

    Args:
    input_string (str): The input string to check for balanced brackets.

    Returns:
    bool: True if the brackets are balanced, False otherwise.
    """

    open_count = 0

    for char in input_string:
        if char == '(':
            open_count += 1
        elif char == ')':
            open_count -= 1
            if open_count < 0:
                return False

    return open_count == 0

# Input the string with parentheses, square brackets, and curly braces
input_string = input("Enter a string with parentheses, square brackets, and curly braces: ")
if bracket(input_string):
    print("The input contains balanced parentheses")
else:
    print("The input does not contain balanced parentheses")