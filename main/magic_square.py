def is_magic_square(matrix):
    n = len(matrix)
    sum_diag1 = 0
    sum_diag2 = 0

    for i in range(n):
        sum_diag1 += matrix[i][i]
        sum_diag2 += matrix[i][n - i - 1]

    if not (sum_diag1 == sum_diag2):
        return False

    for i in range(n):
        sum_row = 0
        sum_col = 0
        for j in range(n):
            sum_row += matrix[i][j]
            sum_col += matrix[j][i]

        if not (sum_row == sum_col == sum_diag1):
            return False

    return True

# Get user input for the size of the matrix
n = int(input("Enter the size of the matrix (number of rows/columns): "))

# Get user input for matrix elements
matrix = []
print("Enter matrix elements row-wise:")
for i in range(n):
    print(f"Enter values for row {i + 1} (separate each value with a space): ", end="")
    
    # Alternative method to obtain row input using a loop
    values = input().split()
    row = []
    for x in values:
        row.append(int(x))
    
    matrix.append(row)

# Display the original matrix
print("\nOriginal Matrix:")
for row in matrix:
    print(row)

# Check if the matrix is a magic square
if is_magic_square(matrix):
    print("\nMagic Square")
else:
    print("\nNot a Magic Square")