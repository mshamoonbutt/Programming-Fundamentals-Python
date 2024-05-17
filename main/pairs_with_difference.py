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

