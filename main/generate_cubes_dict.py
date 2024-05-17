def generate_cubes_dict():
    cubes_dict = {}
    for num in range(1, 6):
        cubes_dict[num] = num ** 3
    return cubes_dict

cubes_dict = generate_cubes_dict()

print(cubes_dict)