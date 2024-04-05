def square_sum():
    """
    Calculate the sum of squares of numbers from 1 to 100.

    This function iterates through numbers from 1 to 100, calculates the square of each number,
    and then adds all the squares together to compute the final sum.

    Parameters:
        None

    Returns:
        None: This function does not return any value. It prints the sum of squares to the console.
    """    
    # Initialize a variable to hold the sum
    sum = 0
    
    # Iterate through numbers from 1 to 100
    for i in range(1, 101):
        # Calculate the square of the current number
        i = i ** 2
        # Add the square to the running sum
        sum += i
    
    # Print the final sum
    print(sum)

# Call the square_sum function
square_sum()
