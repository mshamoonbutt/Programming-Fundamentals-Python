def counter(message):
    # Use a dictionary to store word counts
    word_count = {}

    # Split the message into a list of words
    word_list = message.split()

    for word in word_list:
        # If the word is not in the dictionary, add it with a count of 1
        if word not in word_count:
            word_count[word] = 1
        # If the word is already in the dictionary, increment its count
        else:
            word_count[word] += 1

    # Print the word count for each word
    for word, count in word_count.items():
        print(f"{word}: {count}")

# Get user input for the message
message = input("Enter a message: ")

# Call the counter function
counter(message)