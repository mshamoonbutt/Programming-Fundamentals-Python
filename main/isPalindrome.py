def is_palindrome(input_str):
    """
    Checks if the input string is a palindrome.

    Args:
    input_str (str): The input string to be checked.

    Returns:
    bool: True if the input string is a palindrome, False otherwise.
    """
    # Check if the string is exactly 5 characters long
    if len(input_str) != 5:
        return False

    # Check if the string reads the same forwards and backwards
    is_palindrome = (input_str[0] == input_str[4]) and (input_str[1] == input_str[3])
    
    return is_palindrome

# Get user input
user_input = input("Enter a 5-character string: ")

# Check if it's a palindrome and display the result
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
