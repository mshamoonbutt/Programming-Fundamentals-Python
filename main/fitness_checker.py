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