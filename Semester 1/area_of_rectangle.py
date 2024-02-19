'''Write a program that asks the user for the lengths of the sides of a rectangle. Then
print
• The area and perimeter of the rectangle
• The length of the diagonal'''

import math
l=int(input("Enter value of Length: "))
s=int(input("Enter value of side: "))
area=l*s
p=2*(l+s)
d=math.sqrt(s**2+l**2)
print(f"Area = {area}\nPerimeter = {p}\nDiagonal = {d}")