def remove_elements_at_odd_indexes(input_list):
    return [input_list[i] for i in range(len(input_list)) if i % 2 == 0]

animal_list = ["Cat", "Dog", "Cow", "Bird", "Sparrow"]

result_list = remove_elements_at_odd_indexes(animal_list)

print(result_list)