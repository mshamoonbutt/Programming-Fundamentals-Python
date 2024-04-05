'''Write a program that prompts the user for two integers and then prints
• The sum
• The difference
• The product
• The average
• The distance (absolute value of the difference)
• The maximum (the larger of the two)
• The minimum (the smaller of the two)
Hint: Python defines max and min functions that accept a sequence of values, each
separated with a comma.'''

# Prompt the user to input the first value and store it in the variable x
x = int(input("Enter first value: "))

# Prompt the user to input the second value and store it in the variable y
y = int(input("Enter second value: "))

# Calculate the sum of x and y
sum = x + y

# Calculate the difference between x and y
diff = x - y

# Calculate the product of x and y
pr = x * y

# Calculate the average of x and y
av = (x + y) / 2

# Calculate the absolute difference between x and y
dis = abs(diff)

# Find the maximum value between x and y
max_val = max(x, y)

# Find the minimum value between x and y
min_val = min(x, y)

# Print the calculated values with appropriate labels using f-strings
print(f"Sum: {sum}\nDifference: {diff}\nProduct: {pr}\nAverage: {av}\nDistance: {dis}\nMaximum: {max_val}\nMinimum: {min_val}")
