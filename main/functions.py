#Ques No 1
# Table of number user inputs
def Multiplication(N):
    print(f"Multiplication Table for {N}:")
    for i in range(1, 11):
        result = N * i
        print(f"{N} * {i} = {result}")
N = int(input("Enter Number: "))
Multiplication(N)

#Ques No 2
# Even characters in a string
def get_even_chars(s):
    even_chars = s[::2]
    return even_chars
input_string = input("Enter String: ")
result = get_even_chars(input_string)
print("New String:", result)

#Ques No 3
# First and last characters of a string
def get_first_and_last_chars(s):
    return s[0] + s[-1]
input_string = input("Enter String: ")
result = get_first_and_last_chars(input_string)
print("New string:", result)

#Ques No 4
# Swap first and last characters of a string
def swap_first_and_last(s):
    return s[-1] + s[1:-1] + s[0] * (len(s) > 1)
input_string = input("Enter string: ")
result = swap_first_and_last(input_string)
print("New String:", result)

#Ques No 5
# Reverse Strings
def Reverse_String(s):
    return s[::-1]
input_string = input("Enter String: ")
result = Reverse_String(input_string)
print("New String:", result)





