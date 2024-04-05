#Ques No 1

def traverse(my_list, value):
    exists = False
    for i in my_list:
        if i == value:
            exists = True
            break

    if exists:
        print(f"{value} exists in the list.")
    else:
        print(f"{value} does not exist in the list.")

my_list = [1, 3, 5, 7]
value = int(input("Enter value to check: "))
traverse(my_list, value)


#Ques No 2

def find_pairs_with_difference(array, k):
    result = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if abs(array[i] - array[j]) == k:
                result.append((array[i], array[j]))
    return result

input_array = [1, 5, 3, 4, 2]
k = int(input("Enter value of k: "))

result = find_pairs_with_difference(input_array, k)

print(f"Pairs with a difference of {k}: {result}")


#Ques No 3


#Write a function that takes a 2D list of integers as input and returns the maximum sum of any subarray of the list.

#Ques No 4

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

#Ques No 5

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



