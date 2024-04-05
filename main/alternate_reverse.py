def alternate_k_elements(lst, k):
    """
    Replaces every k elements in the list with the previous element repeated k times,
    starting from the beginning of the list.

    Parameters:
        lst (list): The input list of elements.
        k (int): The number of elements to be replaced with the previous element.

    Returns:
        list: The modified list with every k elements replaced.
    """    
    # Iterate over the list in steps of 'k'
    for i in range(0, len(lst), k):
        # Check if there are enough elements remaining in the list for the next group of 'k' elements
        if i + k <= len(lst):
            # Replace the next 'k' elements with the previous element repeated 'k' times
            lst[i:i+k] = [lst[i-1]] * k
            # Increase 'k' by 3 for the next iteration
            k += 3
    # Return the modified list
    return lst

# Prompt the user to input comma-separated values for the list
user_input = input("Enter comma-separated values for the list: ")
# Convert the input string into a list of integers
lst = [int(x) for x in user_input.split(",")]

# Prompt the user to input the value of 'k'
k = int(input("Enter the value of k: "))

# Call the 'alternate_k_elements' function with the input list and 'k' value
result = alternate_k_elements(lst, k)
# Print the modified list
print("Modified list:", result)
