def multiset_union(set1, set2):
    """
    Compute the union of two multisets represented as dictionaries.

    Args:
    set1 (dict): The first multiset represented as a dictionary.
    set2 (dict): The second multiset represented as a dictionary.

    Returns:
    dict: The dictionary representing the union of the multisets.
    """
    union_dict = set1.copy()

    for key, value in set2.items():
        if key in union_dict:
            union_dict[key] += value
        else:
            union_dict[key] = value

    return union_dict

def multiset_intersection(set1, set2):
    """
    Compute the intersection of two multisets represented as dictionaries.

    Args:
    set1 (dict): The first multiset represented as a dictionary.
    set2 (dict): The second multiset represented as a dictionary.

    Returns:
    dict: The dictionary representing the intersection of the multisets.
    """
    intersection_dict = {}

    for key, value in set1.items():
        if key in set2:
            intersection_dict[key] = min(value, set2[key])

    return intersection_dict

def multiset_difference(set1, set2):
    """
    Compute the difference of two multisets represented as dictionaries.

    Args:
    set1 (dict): The first multiset represented as a dictionary.
    set2 (dict): The second multiset represented as a dictionary.

    Returns:
    dict: The dictionary representing the difference of the multisets.
    """
    difference_dict = set1.copy()

    for key, value in set2.items():
        if key in difference_dict:
            difference_dict[key] = max(difference_dict[key] - value, 0)
        else:
            difference_dict[key] = 0

    return difference_dict

# Example usage:
set1 = {'apple': 2, 'banana': 3, 'orange': 1}
set2 = {'banana': 2, 'grapes': 4, 'orange': 1}

union_result = multiset_union(set1, set2)
intersection_result = multiset_intersection(set1, set2)
difference_result = multiset_difference(set1, set2)

print("Union:", union_result)
print("Intersection:", intersection_result)
print("Difference:", difference_result)