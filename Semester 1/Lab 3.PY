#Ques No 1
user_input = input("Enter a string: ")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)

#Ques No 2
import math
x1 = float(input("Enter the x-coordinate of the first point (x1): "))
y1 = float(input("Enter the y-coordinate of the first point (y1): "))
x2 = float(input("Enter the x-coordinate of the second point (x2): "))
y2 = float(input("Enter the y-coordinate of the second point (y2): "))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
rounded_distance = round(distance)
print(f"The distance between the two points is approximately {rounded_distance} units.")

#Ques No 3
user_input = input("Enter a long string: ")
truncated_string = user_input[:10] + "..."
print(truncated_string)

#Ques No 5
import math
sentence = input("Enter a sentence: ")
sentence_length = len(sentence)
middle_start = math.floor(sentence_length / 4)
middle_length = math.ceil(sentence_length / 2)
middle_substring = sentence[middle_start:middle_start + middle_length]
print("Middle Substring:", middle_substring)


