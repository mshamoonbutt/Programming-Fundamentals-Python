def pass_checker(password):
    """
    Check if a password is strong based on certain criteria.

    The function checks if the password meets the following criteria:
    1. It must be at least 8 characters long.
    2. It must contain at least one uppercase letter.
    3. It must contain at least one lowercase letter.
    4. It must contain at least one digit.
    5. It must contain at least one special character from the set: !@#$%^&*(),.?":{}|<>

    Args:
    password (str): The password to be checked.

    Returns:
    bool: True if the password is strong, False otherwise.
    """

    if len(password) < 8:
        return False
    uppercase = False
    lowercase = False
    digit = False
    special_char = False

    for char in password:
        if char.isupper():
            uppercase = True
        if char.islower():
            lowercase = True
        if char.isdigit():
            digit = True
        if char in "!@#$%^&*(),.?\":{}|<>":
            special_char = True

    return uppercase and lowercase and digit and special_char

# Input the password to check
password = input("Enter password: ")
if pass_checker(password):
    print("Password is strong.")
else:
    print("Password is not strong.")