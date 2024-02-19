#Ques No 1

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
    num_periods = 50 - len(left_str) - len(right_str)
    result = f"{left_str}{'.' * num_periods}{right_str}"
    print(result)

# Get user input
left_str = input("Enter first string: ")
right_str = input("Enter second string: ")

# Call the print_left_right function with the user input
print_left_right(left_str, right_str)



#Ques No 2   

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

#Ques No 3

import math

def distance(x1, y1, x2, y2):
    """
    Calculate the distance between two points in the Cartesian plane.

    Args:
    x1 (float): x-coordinate of the first point.
    y1 (float): y-coordinate of the first point.
    x2 (float): x-coordinate of the second point.
    y2 (float): y-coordinate of the second point.

    Returns:
    float: The distance between the two points.
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def radius(center_x, center_y, point_x, point_y):
    """
    Calculate the radius of a circle given the center and a point on the circle.

    Args:
    center_x (float): x-coordinate of the circle's center.
    center_y (float): y-coordinate of the circle's center.
    point_x (float): x-coordinate of a point on the circle.
    point_y (float): y-coordinate of a point on the circle.

    Returns:
    float: The radius of the circle.
    """
    return distance(center_x, center_y, point_x, point_y)

def circumference(radius):
    """
    Calculate the circumference of a circle given its radius.

    Args:
    radius (float): The radius of the circle.

    Returns:
    float: The circumference of the circle.
    """
    return 2 * math.pi * radius

def area(radius):
    """
    Calculate the area of a circle given its radius.

    Args:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return math.pi * radius ** 2

center_x = float(input("Enter the x-coordinate of the center: "))
center_y = float(input("Enter the y-coordinate of the center: "))
point_x = float(input("Enter the x-coordinate of a point on the circle: "))
point_y = float(input("Enter the y-coordinate of a point on the circle: "))

circle_radius = radius(center_x, center_y, point_x, point_y)
circle_diameter = 2 * circle_radius
circle_circumference = circumference(circle_radius)
circle_area = area(circle_radius)

print(f"Radius of the circle: {circle_radius:.2f}")
print(f"Diameter of the circle: {circle_diameter:.2f}")
print(f"Circumference of the circle: {circle_circumference:.2f}")
print(f"Area of the circle: {circle_area:.2f}")

#Ques No 4

def calculate_billing_amount(hourly_rate, consulting_time, low_income):
    """
    Calculate the billing amount for tax assistance.

    Args:
    hourly_rate (float): The hourly rate for tax assistance.
    consulting_time (int): The total consulting time in minutes.
    is_low_income (bool): True if the person has low income, False otherwise.

    Returns:
    float: The billing amount.
    """
    if low_income:
        if consulting_time <= 30:
            return 0.0  # No charges for low-income clients with <=30 minutes of consulting time
        else:
            time_over_30_minutes = consulting_time - 30
            service_charges = hourly_rate * 0.40 * (time_over_30_minutes / 60)
            return service_charges
    else:
        if consulting_time <= 20:
            return 0.0  # No service charges for others with <=20 minutes of consulting time
        else:
            time_over_20_minutes = consulting_time - 20
            service_charges = hourly_rate * 0.70 * (time_over_20_minutes / 60)
            return service_charges

# Prompt the user for input
hourly_rate = float(input("Enter the hourly rate for tax assistance: $"))
consulting_time = int(input("Enter the total consulting time in minutes: "))
low_income = input("Is the person low-income (yes/no)? ").strip().lower() == "yes"

# Calculate the billing amount
billing_amount = calculate_billing_amount(hourly_rate, consulting_time,low_income)

# Display the billing amount
print(f"Billing Amount: ${billing_amount:.2f}")

#Ques No 5
def card_check(card_number):
    """
    Check if a credit card number is valid and provide intermediate steps.

    Args:
    card_number (str): A string representing an 8-digit credit card number.

    Returns:
    str: A message indicating if the number is a valid card number or not.
    """

    # Step 1: Calculate the sum (A) of every other digit starting from the rightmost digit
    sum_a = 0
    for i in range(7, -1, -2):
        digit = int(card_number[i])
        sum_a += digit

    print(f"A: {sum_a}")

    # Step 2: Calculate the digit-sequence formed by doubling and adding all digits not included in A
    sum_b = 0
    sequence = ""
    for i in range(6, -1, -2):
        digit = int(card_number[i])
        doubled_digit = digit * 2
        sequence += str(doubled_digit)

        if doubled_digit >= 10:
            sum_b += doubled_digit // 10 + doubled_digit % 10
        else:
            sum_b += doubled_digit

    print(f"Sequence: {sequence}")
    print(f"B: {sum_b}")

    # Step 3: Calculate the total sum (A + B)
    total_sum = sum_a + sum_b
    print(f"A+B: {total_sum}")

    # Check if the total sum's last digit is 0
    if total_sum % 10 == 0:
        return "Valid card number"
    else:
        valid_digit = (10 - (total_sum % 10)) % 10
        return f"Invalid card number. The last digit to make it valid is: {valid_digit}"

# Get user input and call the function
card_number = input("Please input the credit card number (8 digits): ")
result = card_check(card_number)
print(result)


#Ques No 6

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

    
