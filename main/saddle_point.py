def find_saddle_point(matrix, n):
    for i in range(n):
        min_row_value = matrix[i][0]
        col_index = 0

        for j in range(1, n):
            if min_row_value > matrix[i][j]:
                min_row_value = matrix[i][j]
                col_index = j

        k = 0
        for k in range(n):
            if min_row_value < matrix[k][col_index]:
                break
            k += 1

        if k == n:
            print("Value of Saddle Point:", min_row_value)
            return True

    return False

# Get user input for the size of the matrix
n = int(input("Enter the size of the matrix (number of rows/columns): "))

# Get user input for matrix elements
matrix = []
print("Enter matrix elements row-wise:")
for i in range(n):
    print(f"Enter values for row {i + 1} (separate each value with a space): ", end="")
    values = input().split()
    row = [int(x) for x in values]
    matrix.append(row)

# Display the original matrix
print("\nOriginal Matrix:")
for row in matrix:
    print(row)

saddle_point_found = find_saddle_point(matrix, n)
if not saddle_point_found:
    print("\nNo Saddle Point found.")
# Replace the line with any other condition
else:
    print("\nSaddle Point found.")