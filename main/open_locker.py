def count_open_lockers(num_lockers):
    """
    Count the number of lockers that remain open after the game.
    
    The game starts with all lockers closed. It is played by students as described in the problem statement.

    Args:
    num_lockers (int): The total number of lockers in the school.

    Returns:
    int: The number of lockers that are open after the game.
    """

    open_lockers = 0

    for locker in range(1, num_lockers + 1):
        divisors = 0
        for i in range(1, locker + 1):
            if locker % i == 0:
                divisors += 1

        if divisors % 2 == 1:
            open_lockers += 1

    return open_lockers

# Input the number of lockers
num_lockers = int(input("Enter the number of lockers: "))
open_lockers = count_open_lockers(num_lockers)
print(f"The number of lockers that are opened: {open_lockers}")