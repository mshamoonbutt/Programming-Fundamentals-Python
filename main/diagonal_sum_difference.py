def diagonal_sum_difference(matrix, size):
    d1_sum = 0
    d2_sum = 0

    for i in range(size):
        for j in range(size):
            if i == j:
                d1_sum += matrix[i][j]
            if i == size - j - 1:
                d2_sum += matrix[i][j]

    return abs(d1_sum - d2_sum)

# Get user input for the size of the square matrix
size = int(input("Enter the size of the square matrix: "))

# Get user input for matrix elements
matrix = []
print("Enter matrix elements row-wise:")
for i in range(size):
    row = []
    values = input(f"Enter values for row {i + 1} (separate each value with a space): ").split()
    for x in values:
        row.append(int(x))
    matrix.append(row)
result = diagonal_sum_difference(matrix, size)
print("Absolute Difference between Diagonal Sums:", result)