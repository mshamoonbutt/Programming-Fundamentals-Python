'''Write a program that prompts the user for a radius and then prints
• The area and circumference of a circle with that radius
• The volume and surface area of a sphere with that radius'''

import math
r=int(input("Enter value of radius: "))
area=math.pi*r**2
circumference=2*math.pi*r
volume=(4/3)*math.pi*r**3
surface_area=4*math.pi*r**2
print(f"Area = {area}\nCircumference = {circumference}\nVolume = {volume}\nSurface Area = {surface_area}")