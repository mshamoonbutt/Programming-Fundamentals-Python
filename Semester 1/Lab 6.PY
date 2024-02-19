#Ques No 1

def print_primes(num):
    
    for num in range(2, num + 1):
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)

num = int(input("Enter a number: "))
print("First", num, "Prime numbers are:\n")            
print_primes(num)


#Ques No 2

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


#Ques No 3

def are_anagrams(x, y):
    # Remove spaces and convert to lowercase
    x = x.replace(" ", "").lower()
    y = y.replace(" ", "").lower()

    # Check if the lengths are equal
    if len(x) != len(y):
        return False

    # Count characters
    for char in x:
        if x.count(char) != y.count(char):
            return False
    return True  

# Input two strings from the user
x = input("Enter the first string: ")
y = input("Enter the second string: ")

if are_anagrams(x, y):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


#Ques No 4
n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()    


#Ques No 5

def print_table(n, m):
    # Print the header row
    print("X |", end=" ")
    for i in range(1, m + 1):
        print(f"{i:3}", end=" ")
    print("\n" + "-" * (4 * (m + 2)))  # Print a separator line

    # Generate and print the multiplication table
    for i in range(1, n + 1):
        print(f"{i:1} |", end=" ")
        for j in range(1, m + 1):
            print(f"{i * j:3}", end=" ")
        print()

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
print_table(n, m)

















