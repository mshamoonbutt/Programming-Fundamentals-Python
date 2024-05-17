def is_prime(num):
    """
    Check if a number is prime.

    Args:
    num (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Twin prime pairs within the range:")
# Iterate through the range from 'start' to 'end - 1'
for num in range(start, (end - 1)):
    # Check if 'num' and 'num + 2' are prime, indicating a twin prime pair
    if is_prime(num) and is_prime(num + 2):
        print(num, "and", num + 2)