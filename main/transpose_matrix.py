def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed_matrix = []
    for _ in range(cols):
        transposed_matrix.append([0] * rows)

    for i in range(cols):
        for j in range(rows):
            transposed_matrix[i][j] = matrix[j][i]

    return transposed_matrix

# Get user input for the matrix
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
for i in range(rows):
    row = [int(x) for x in input(f"Enter values for row {i + 1} (separate each value with a space): ").split()]
    matrix.append(row)

# Display the original matrix
print("\nOriginal Matrix:")
for row in matrix:
    print(row)

# Calculate and display the transposed matrix using the defined function
result = transpose_matrix(matrix)
print("\nTransposed Matrix:")
for row in result:
    print(row)