#Ques No 1

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

#Ques No 2

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

#Ques No 3

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
    
    
#Ques No 4

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
    

#Ques No 5

def transform_matrix(input_matrix):
    output_matrix = []
    for row in input_matrix:
        new_row = []
        for num in row:
            if num % 2 == 0:
                new_row.append(0)
            else:
                new_row.append(1)
        output_matrix.append(new_row)

    return output_matrix


rows_count = int(input("Enter the number of rows: "))
cols_count = int(input("Enter the number of columns: "))

user_matrix = []
print("Enter matrix elements:")
for i in range(rows_count):
    row = []
    for j in range(cols_count):
        element = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
        row.append(element)
    user_matrix.append(row)

transformed_matrix = transform_matrix(user_matrix)

print("Original Matrix:")
for row in user_matrix:
    print(row)
print("Transformed Matrix:")
for row in transformed_matrix:
    print(row)


   