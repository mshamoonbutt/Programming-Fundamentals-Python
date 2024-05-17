def are_anagrams(x, y):
    # Remove spaces and convert to lowercase
    x = x.replace(" ", "").lower()
    y = y.replace(" ", "").lower()

    # Check if the lengths are equal
    if len(x) != len(y):
        return False

    # Count characters
    for char in x:
        if x.count(char) != y.count(char):
            return False
    return True  

# Input two strings from the user
x = input("Enter the first string: ")
y = input("Enter the second string: ")

if are_anagrams(x, y):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")