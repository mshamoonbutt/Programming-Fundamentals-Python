def count_occurrences(filename, word):
    try:
        with open(filename, 'r') as file_obj:
            file_content = file_obj.read()
            occurrences_count = 0

            # Custom implementation for counting occurrences
            content_lowercase = file_content.lower()
            word_lowercase = word.lower()

            i = 0
            while i < len(content_lowercase):
                index = content_lowercase.find(word_lowercase, i)
                if index == -1:
                    break
                occurrences_count += 1
                i = index + 1

            return occurrences_count
    except FileNotFoundError:
        return -1

def main():
    file_name_input = input("Enter the name of the file: ")
    search_word_input = input("Enter the word to search: ")

    occurrences_result = count_occurrences(file_name_input, search_word_input)

    if occurrences_result == -1:
        print(f"Error: File '{file_name_input}' not found.")
    else:
        print(f"{search_word_input} appears {occurrences_result} times in the file.")

if __name__ == "__main__":
    main()