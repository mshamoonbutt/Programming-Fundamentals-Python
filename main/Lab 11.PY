#Ques No 1
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


#Ques No 2
def replace_word(input_file, output_file, search, replacement):
    try:
        with open(input_file, 'r') as file_input:
            content = file_input.read()

            # Custom implementation for replacing word
            replaced_content = ""
            i = 0
            while i < len(content):
                index = content.lower().find(search.lower(), i)
                if index == -1:
                    replaced_content += content[i:]
                    break
                replaced_content += content[i:index] + replacement
                i = index + len(search)

        with open(output_file, 'w') as file_output:
            file_output.write(replaced_content)

        # Custom implementation for counting occurrences
        occurrences = 0
        i = 0
        while i < len(content):
            index = content.lower().find(search.lower(), i)
            if index == -1:
                break
            occurrences += 1
            i = index + 1

        return occurrences
    except FileNotFoundError:
        return -1

def main():
    input_file = input("Enter input file name: ")
    output_file = input("Enter output file name: ")
    search_word = input("Enter word to search: ")
    replacement_word = input("Enter replacement word: ")

    replacements = replace_word(input_file, output_file, search_word, replacement_word)

    if replacements == -1:
        print(f"Error: Input file '{input_file}' not found.")
    else:
        print(f"I replaced {replacements} instance(s) of {search_word} with {replacement_word}\n")

if __name__ == "__main__":
    main()


#Ques No 3
def calculate_mean(scores):
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    mean = total / count
    return mean

def main():
    try:
        with open('test.in', 'r') as file:
            n = int(file.readline().strip())
            scores = []
            for _ in range(n):
                score = int(file.readline().strip())
                scores.append(score)

        mean = calculate_mean(scores)
        print(f'Mean: {mean}')
    except FileNotFoundError:
        print('Error: File test.in not found.')

if __name__ == "__main__":
    main()
