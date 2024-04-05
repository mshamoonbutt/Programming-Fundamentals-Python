'''Write a program that prompts the user for a radius and then prints
• The area and circumference of a circle with that radius
• The volume and surface area of a sphere with that radius'''

import math

# Prompt the user to input the value of the radius
r = int(input("Enter value of radius: "))

# Calculate the area of the circle
area = math.pi * r**2

# Calculate the circumference of the circle
circumference = 2 * math.pi * r

# Calculate the volume of the sphere
volume = (4/3) * math.pi * r**3

# Calculate the surface area of the sphere
surface_area = 4 * math.pi * r**2

# Print the calculated values
print(f"Area = {area}\nCircumference = {circumference}\nVolume = {volume}\nSurface Area = {surface_area}")
