import math
x1 = float(input("Enter the x-coordinate of the first point (x1): "))
y1 = float(input("Enter the y-coordinate of the first point (y1): "))
x2 = float(input("Enter the x-coordinate of the second point (x2): "))
y2 = float(input("Enter the y-coordinate of the second point (y2): "))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
rounded_distance = round(distance)
print(f"The distance between the two points is approximately {rounded_distance} units.")