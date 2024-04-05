'''Write a program that asks the user for the lengths of the sides of a rectangle. Then
print
• The area and perimeter of the rectangle
• The length of the diagonal'''

import math

# Prompt the user to input the value of the length and side
l = int(input("Enter value of Length: "))
s = int(input("Enter value of side: "))

# Calculate the area of the rectangle
area = l * s

# Calculate the perimeter of the rectangle
p = 2 * (l + s)

# Calculate the length of the diagonal using the Pythagorean theorem
d = math.sqrt(s**2 + l**2)

# Print the calculated values
print(f"Area = {area}\nPerimeter = {p}\nDiagonal = {d}")
