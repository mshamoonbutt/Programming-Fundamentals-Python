#Write a program that displays the dimensions of a letter-size (8.5 × 11 inch) sheet of paper in millimeters. There are 25.4 millimeters per inch. Use constants and comments in your program.
# Constants
INCH_TO_MM = 25.4
LETTER_WIDTH_INCH = 8.5
LETTER_HEIGHT_INCH = 11.0

# Calculate dimensions in millimeters
letter_width_mm = LETTER_WIDTH_INCH * INCH_TO_MM
letter_height_mm = LETTER_HEIGHT_INCH * INCH_TO_MM

# Display the dimensions
print("Letter size (8.5 × 11 inch) sheet of paper dimensions:")
print(f"Width: {letter_width_mm:.2f} mm")
print(f"Height: {letter_height_mm:.2f} mm")