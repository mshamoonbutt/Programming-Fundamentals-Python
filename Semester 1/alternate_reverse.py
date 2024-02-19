def alternate_k_elements(lst, k):
    for i in range(0, len(lst), k):
        if i + k <= len(lst):
            lst[i:i+k] = [lst[i-1]] * k
            k += 3
    return lst

user_input = input("Enter comma-separated values for the list: ")
lst = [int(x) for x in user_input.split(",")]

k = int(input("Enter the value of k: "))

result = alternate_k_elements(lst, k)
print("Modified list:", result)