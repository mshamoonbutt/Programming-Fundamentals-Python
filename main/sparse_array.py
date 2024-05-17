def sparseArraySum(a, b):
    """
    Compute the vector sum of two sparse arrays represented as dictionaries.

    Args:
    a (dict): The first sparse array represented as a dictionary.
    b (dict): The second sparse array represented as a dictionary.

    Returns:
    dict: The dictionary representing the vector sum of the sparse arrays.
    """
    result = {}

    for key in set(a.keys()).union(b.keys()):
        result[key] = a.get(key, 0) + b.get(key, 0)

    return result

# Example usage:
sparse_array_a = {5: 4, 9: 2, 10: 9}
sparse_array_b = {2: 3, 5: 1, 9: 5}

result_sum = sparseArraySum(sparse_array_a, sparse_array_b)
print("Vector Sum:", result_sum)