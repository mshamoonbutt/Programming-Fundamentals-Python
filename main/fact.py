def factorial(n):
    if n < 0:
        return "Factorial is not valid for negative numbers."
    elif n == 0:
        return 0
    else:
        factorial = 1
        while n > 0:
            factorial *= n
            n -= 1
        return factorial

# Input from the user
n = int(input("Enter a non-negative integer: "))

result = factorial(n)
print(f"The factorial of {n} is: {result}")