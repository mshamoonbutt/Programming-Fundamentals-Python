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