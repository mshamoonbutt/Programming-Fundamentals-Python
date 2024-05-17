def column_products(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    if num_cols == 0:
        return []

    result = [1] * num_cols

    for col in range(num_cols):
        for row in range(num_rows):
            result[col] *= matrix[row][col]

    return result

input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = column_products(input_matrix)

print("Product of each column:", result)