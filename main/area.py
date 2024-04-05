def area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
        length (int): The length of the rectangle.
        width (int): The width of the rectangle.

    Returns:
        None: The function prints the calculated area of the rectangle.
    """    
    # Calculate the area of the rectangle
    area = length * width
    # Print the calculated area
    print(f"Area of rectangle is {area}")

# Prompt the user to input the length of the rectangle
length = int(input("Enter Length: "))
# Prompt the user to input the width of the rectangle
width = int(input("Enter Width: "))

# Call the 'area' function with the user-provided length and width
area(length, width)
