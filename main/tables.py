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