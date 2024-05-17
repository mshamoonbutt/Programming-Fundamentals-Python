def count_unique_elements(matrix):
    unique_elements = []

    for row in matrix:
        for element in row:
            exists = False
            for unique_element in unique_elements:
                if element == unique_element:
                    exists = True
                    break
            if not exists:
                unique_elements.append(element)

    return len(unique_elements)

input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3],
    [7, 8, 5]
]

result = count_unique_elements(input_matrix)

print("Count of unique elements:", result)