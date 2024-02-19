#Ques No 1
def leap_year(year):
    """
    Check if a year is a leap year.

    Args:
    year (int): The year to check.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
        return True
    return False

def days_in_month_calculation(m, year):
    """
    Calculate the number of days in a specific month.

    Args:
    m (int): The month (1-12) to calculate the days for.
    year (int): The year for potential leap year calculation.

    Returns:
    int: The number of days in the specified month.
    """
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    elif m == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    else:
        return 30

# Input date, month, and year
month = int(input("Enter month (1-12): "))
date = int(input("Enter date (1-31): "))
year = int(input("Enter year (0-2023): "))

m = 1
days_in_month = 0
while m <= month:
    if m == month:
        days_in_month += date
    else:
        days_in_month += days_in_month_calculation(m, year)
    m += 1

# Printing number of days
output_days = days_in_month
print(f"The day number of {month}-{date}-{year} is {output_days}")



#Ques No 2

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

 
    
#Ques No 3

def is_prime(num):
    """
    Check if a number is prime.

    Args:
    num (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Twin prime pairs within the range:")
# Iterate through the range from 'start' to 'end - 1'
for num in range(start, (end - 1)):
    # Check if 'num' and 'num + 2' are prime, indicating a twin prime pair
    if is_prime(num) and is_prime(num + 2):
        print(num, "and", num + 2)



#Ques No 4

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

        
       
#Ques No 5

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


#Ques No 6

def fitness(f, g, h):
    """
    Determine the appropriate weight range based on gender, frame, and height.

    Args:
    f (str): Frame size ('small', 'medium', or 'large').
    g (str): Gender ('M' for male or 'F' for female).
    h (int): Height in inches.

    Returns:
    None: Prints the appropriate weight range based on the input.

    Note:
    The function provides a weight range based on gender, frame size, and height.
    """
    if g == 'F' or g == 'f':
        if f == 'small':
            if h >= 58 and h <= 62:
                print("Appropriate weight range is 50-52 kg")
            elif h > 62 and h <= 64:
                print("Appropriate weight range is 54-56 kg")
            elif h > 64 and h <= 66:
                print("Appropriate weight range is 58-60 kg")
            elif h > 66 and h <= 70:
                print("Appropriate weight range is 62-64 kg")
            else:
                print("Invalid input")                  
        if f == 'medium':
            if h >= 58 and h <= 62:
                print("Appropriate weight range is 51-53 kg")
            elif h > 62 and h <= 64:
                print("Appropriate weight range is 55-57 kg")
            elif h > 64 and h <= 66:
                print("Appropriate weight range is 59-61 kg")
            elif h > 66 and h <= 70:
                print("Appropriate weight range is 63-65 kg")
            else:
                print("Invalid input")                  
        if f == 'large':
            if h >= 58 and h <= 62:
                print("Appropriate weight range is 52-54 kg")
            elif h > 62 and h <= 64:
                print("Appropriate weight range is 56-58 kg")
            elif h > 64 and h <= 66:
                print("Appropriate weight range is 60-62 kg")
            elif h > 66 and h <= 70:
                print("Appropriate weight range is 64-66 kg")
            else:
                print("Invalid input")                  
    elif g == 'M' or g == 'm':
        if f == 'small':
            if h >= 65 and h <= 68:
                print("Appropriate weight range is 65-67 kg")
            elif h > 68 and h <= 70:
                print("Appropriate weight range is 69-71 kg")
            elif h > 70 and h <= 74:
                print("Appropriate weight range is 73-75 kg")
            elif h > 74 and h <= 78:
                print("Appropriate weight range is 77-79 kg")
            else:
                print("Invalid input")                  
        if f == 'medium':
            if h >= 65 and h <= 68:
                print("Appropriate weight range is 66-68 kg")
            elif h > 68 and h <= 70:
                print("Appropriate weight range is 70-72 kg")
            elif h > 70 and h <= 74:
                print("Appropriate weight range is 74-76 kg")
            elif h > 74 and h <= 78:
                print("Appropriate weight range is 78-80 kg")
            else:
                print("Invalid input")                  
        if f == 'large':
            if h >= 65 and h <= 68:
                print("Appropriate weight range is 67-69 kg")
            elif h > 68 and h <= 70:
                print("Appropriate weight range is 71-73 kg")
            elif h > 70 and h <= 74:
                print("Appropriate weight range is 75-77 kg")
            elif h > 74 and h <= 78:
                print("Appropriate weight range is 79-81 kg")
            else:
                print("Invalid input")    
    else:
        print("Invalid input")

# Take user inputs and call the fitness function
f = input("Enter your Frame (small, medium, or large): ").lower()
g = input("Enter your Gender (M or F): ").upper()
h = int(input("Enter your height in inches: "))
fitness(f, g, h)


#Ques No 7

def sequence(x):

    """
    Calculate the Collatz sequence for a given integer and print each value.
    
    Parameters:
    x (int): The initial integer value for the Collatz sequence.
    
    Returns:
    int: The value of k where a_k equals 1.
    """
    
    k = 0

    # Print the initial value a0
    print(f"a{k} = {x}")

    # Calculate the sequence and display each value
    while x != 1:
        k += 1
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        print(f"a{k} = {x}")

    return k

# Input the value of x from the user
x = int(input("Enter the value of x: "))

# Calculate k, the number of iterations until ak equals 1
k = sequence(x)

# Output the result
print(f"The value of k where a_k = 1 for x = {x} is k = {k}")

    
    
#Ques No 8

def count_open_lockers(num_lockers):
    """
    Count the number of lockers that remain open after the game.
    
    The game starts with all lockers closed. It is played by students as described in the problem statement.

    Args:
    num_lockers (int): The total number of lockers in the school.

    Returns:
    int: The number of lockers that are open after the game.
    """

    open_lockers = 0

    for locker in range(1, num_lockers + 1):
        divisors = 0
        for i in range(1, locker + 1):
            if locker % i == 0:
                divisors += 1

        if divisors % 2 == 1:
            open_lockers += 1

    return open_lockers

# Input the number of lockers
num_lockers = int(input("Enter the number of lockers: "))
open_lockers = count_open_lockers(num_lockers)
print(f"The number of lockers that are opened: {open_lockers}")
    
        




