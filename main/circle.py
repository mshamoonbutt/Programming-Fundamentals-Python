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
