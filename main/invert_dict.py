def invert_dict(input_dict):
    """
    Invert the keys and values of a dictionary. Handles cases where multiple keys have the same value.

    Args:
    input_dict (dict): The input dictionary.

    Returns:
    dict: The inverted dictionary.
    """
    inverted_dict = {}

    for key, value in input_dict.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]

    return inverted_dict

# Example usage:
original_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
inverted_result = invert_dict(original_dict)

print("Original Dictionary:", original_dict)
print("Inverted Dictionary:", inverted_result)