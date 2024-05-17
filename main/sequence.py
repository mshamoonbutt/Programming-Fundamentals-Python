def sequence(x):

    """
    Calculate the Collatz sequence for a given integer and print each value.
    
    Parameters:
    x (int): The initial integer value for the Collatz sequence.
    
    Returns:
    int: The value of k where a_k equals 1.
    """
    
    k = 0

    # Print the initial value a0
    print(f"a{k} = {x}")

    # Calculate the sequence and display each value
    while x != 1:
        k += 1
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        print(f"a{k} = {x}")

    return k

# Input the value of x from the user
x = int(input("Enter the value of x: "))

# Calculate k, the number of iterations until ak equals 1
k = sequence(x)

# Output the result
print(f"The value of k where a_k = 1 for x = {x} is k = {k}")
