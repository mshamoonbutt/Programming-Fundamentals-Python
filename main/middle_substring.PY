import math
sentence = input("Enter a sentence: ")
sentence_length = len(sentence)
middle_start = math.floor(sentence_length / 4)
middle_length = math.ceil(sentence_length / 2)
middle_substring = sentence[middle_start:middle_start + middle_length]
print("Middle Substring:", middle_substring)


