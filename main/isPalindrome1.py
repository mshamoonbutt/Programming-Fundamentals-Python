def is_palindrome(string):
    cleaned_string = string.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]

# Take a sentence from the user as input
user_input = input("Enter a sentence to check if it's a palindrome: ")

result = is_palindrome(user_input)

if result:
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')