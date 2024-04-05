# Create an empty dictionary
cube_dict = {}

# Use a loop to iterate through numbers from 1 to 5
for num in range(1, 6):
    # Assign the cube of the current number as the value for the key in the dictionary
    cube_dict[num] = num**3

# Print the resulting dictionary
print(cube_dict)